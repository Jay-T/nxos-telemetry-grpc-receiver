from concurrent import futures
import logging

import grpc
from google.protobuf import json_format

import mdt_dialout_pb2
import mdt_dialout_pb2_grpc
import telemetry_bis_pb2

class gRPCMdtDialout(mdt_dialout_pb2_grpc.gRPCMdtDialoutServicer):
    def MdtDialout(self, request_iterator, context):
        for response in request_iterator:
            # logging.info(response)  # print not decoded received message.
            tele_msg = telemetry_bis_pb2.Telemetry()
            tele_msg.ParseFromString(response.data)
            parsed_data = json_format.MessageToJson(tele_msg) # get data in json
            logging.info(parsed_data) # print received telemetry data as json
            yield 


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mdt_dialout_pb2_grpc.add_gRPCMdtDialoutServicer_to_server(gRPCMdtDialout(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        serve()
    except(KeyboardInterrupt):
        logging.info('Manually stopped by keyboard interruption')