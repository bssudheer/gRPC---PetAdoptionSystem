import grpc
import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc

def run():
    # Connect to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    
    while True:
        # Display the menu
        print("\n--- Calculator Menu ---")
        print("1: Add")
        print("2: Multiply")
        print("3: Exit")
        choice = input("Select an operation (1, 2, 3): ")

        if choice == '1' or choice == '2':
            try:
                # Get numbers from the user
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            # Call the appropriate RPC method
            if choice == '1':
                response = stub.Add(calculator_pb2.OperationRequest(num1=num1, num2=num2))
                print(f"Result of {num1} + {num2} = {response.result}")
            elif choice == '2':
                response = stub.Multiply(calculator_pb2.OperationRequest(num1=num1, num2=num2))
                print(f"Result of {num1} * {num2} = {response.result}")
        
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    run()
