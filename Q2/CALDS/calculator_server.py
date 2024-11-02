import grpc
from concurrent import futures
import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc

# Define the CalculatorServicer class
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.OperationResponse(result=result)
    
    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.OperationResponse(result=result)

# Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Python gRPC server running...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
