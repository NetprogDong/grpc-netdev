#! /usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
import time
import grpc
import lib.h3c.grpc_dialout_pb2 as h3c_grpc_dialout_pb2
import lib.h3c.grpc_dialout_pb2_grpc as h3c_grpc_dialout_pb2_grpc


class GRPC_Dialout(h3c_grpc_dialout_pb2_grpc.GRPCDialoutServicer):
    def Dialout(self, request, context):
        for info in request:
            # 打印proto文件中定义的DeviceInfo消息
            print('deviceName: %s' % info.deviceMsg.deviceName)
            print('deviceModel: %s' % info.deviceMsg.deviceModel)
            print('producerName: %s' % info.deviceMsg.producerName)
            print('--------------------------------------')
            # 打印proto文件中定义的sensorPath消息
            print('sensorPath: %s' % info.sensorPath)
            # 打印指定sensorPath监控项的监控数据消息
            print('Data as below')
            print info.jsonData
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