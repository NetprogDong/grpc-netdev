#! /usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
import time
import grpc
import lib.h3c.grpc_dialout_pb2 as h3c_grpc_dialout_pb2
import lib.h3c.grpc_dialout_pb2_grpc as h3c_grpc_dialout_pb2_grpc
from influxdb import InfluxDBClient
import json

class GRPC_Dialout(h3c_grpc_dialout_pb2_grpc.GRPCDialoutServicer):
    def Dialout(self, request, context):
        influx_client = InfluxDBClient('dbserver_ip', 8086, 'admin', 'adminpasswd', 'mydb')
        json_body = []
        for info in request:
            deviceName = info.deviceMsg.deviceName
            deviceModel = info.deviceMsg.deviceModel
            datatext = json.loads(info.jsonData)
            if info.sensorPath == u'Ifmgr/Statistics':
                timeStamp = long(datatext['Notification']['Timestamp'] + '000000')
                for interf in datatext['Notification']['Ifmgr']['Statistics']['Interface']:
                    IfIndex = interf['IfIndex']
                    IfName = interf['Name']

                    InRate = interf['InRate'] * 8
                    OutRate = interf['OutRate'] * 8

                    IfRate_Data = {
                        'measurement': 'IfRate',
                        'tags': {
                            'hostname': deviceName,
                            'ifindex': IfIndex,
                            'ifname': IfName,
                            'model': deviceModel
                        },
                        'time': timeStamp,
                        'fields': {
                            'inrate': InRate,
                            'outrate': OutRate
                        }
                    }
                    json_body.append(IfRate_Data)
                influx_client.write_points(json_body)


        return h3c_grpc_dialout_pb2.DialoutResponse(response='hello')


def serve():
    # 这里通过threadpool来并发处理server的任务,最大并发数量10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 将对应的任务处理函数添加到rpc server中
    h3c_grpc_dialout_pb2_grpc.add_GRPCDialoutServicer_to_server(GRPC_Dialout(), server)
    # 这里使用的非安全接口,绑定tcp端口号44444,监听本地任意ip
    server.add_insecure_port('0.0.0.0:44444')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()