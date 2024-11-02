## CSE-5306-004-DISTRIBUTED SYSTEMS
## Project Assignment 2: gRPC-Backed Virtual Pet Adoption System

## Group 20: Srinivas Sudheer Reddy Buchipalli – 1002149811 & Ali Ashan


## Q1 Part 1:
Prerequisites": Install Node veriosn greater than 8.13 : npm i


# Clone the repository to get the example code
$ git clone -b @grpc/grpc-js@1.9.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc-node
# Navigate to the node example
$ cd grpc-node/examples

# Install the example's dependencies
$ npm install
# Navigate to the dynamic codegen "hello, world" Node example:
$ cd helloworld/dynamic_codegen


## Run a gRPC application


Run ethe server:
node greeter_server.js

Run the client:

node greeter_client.js

## Q1 Part 2
Prerequisites

1. python -m pip install --upgrade pip
2. python -m pip install grpcio
3. python -m pip install grpcio-tools

# Clone the repository to get the example code:
$ git clone -b v1.66.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
# Navigate to the "hello, world" Python example:
$ cd grpc/examples/python/helloworld

## Run GRPC Application:

## Run the server:
python greeter_server.py

## Run the Clioent:

python greeter_client.py

## Generate gRPC code:
Using CMD promt of IDE:

python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto


## Make cahnges to existing codE:

Again run the server and client with above commands


## Q2

Prerequisites
1. python -m pip install --upgrade pip
2. python -m pip install grpcio
3. python -m pip install grpcio-tools
4.Install Node veriosn greater than 8.13 : npm i

## Now run the server and client:

python sever.py and node client.js || python client.py and node server.js

Post running it we can see a menu in client side running saying like menu

Calculator Menu:
1. Addition
2. Multiplication
3. Exit

Select an operation (1,2,3) : 1

Enter the first Number: 3

Enter the second Number: 3
Result of 3 + 3 = 6

Similarly we do for multiplication.

select option 3 to exit out.


## Q3

# Pet Adoption System with gRPC

This project is a Pet Adoption System built using gRPC. It consists of a Node.js server, a Python client, and a worker script. The system allows users to register pets, adopt them, and search for pets. The project is containerized using Docker for easy deployment.

## Project Structure
Main Files needed for this project set-up

GRPC/
├──  docker_client.py          # Docker client file for the Python client
├──  docker_server.js          # Docker server file for the Node.js server
├──  pet_adoption.proto        # Protocol Buffers file defining gRPC services and messages
├──  server.js                 # Node.js server implementation
├──  client.py                 # Python client implementation
├──  worker.js                 # Worker script for handling requests
└──  test_pet_adoption.py      # Unit tests for the pet adoption system



## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (version >= 14)
- [Python](https://www.python.org/) (version >= 3.7)
- [Docker](https://www.docker.com/) (if you want to run the project in containers)
- [gRPC](https://grpc.io/docs/languages/) libraries for both Node.js and Python

## Setup Instructions

1. cd GRPC
2. npm install grpc
3. python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install grpcio grpcio-tools
4. compile the proto file:
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pet_adoption.proto

5. Run the sever code: node server.js
6. Run the cliemnt code: python client.py

## Setup Instructions for Docker

docker build -t pet-adoption-server -f docker_server .
docker build -t pet-adoption-client -f docker_client .

## Setup Instructions for Running Test Cases:

python test_pet_adoption.py

Test Cases Overview for Pet Adoption System

1. Test Register Pet:
   - Purpose: Verify that a pet can be successfully registered in the system.
   - Method: test_register_pet
   - Assertion: Checks if the response message confirms the registration of the pet.

2. Test Fetch Pets:
   - Purpose: Ensure that registered pets can be fetched from the system.
   - Method: test_fetch_pets
   - Assertion: Confirms that the list of pets is not empty after registering a new pet.

3. Test Adopt Pet:
   - Purpose: Validate that a pet can be adopted successfully.
   - Method: test_adopt_pet
   - Assertion: Checks if the adoption response message confirms the successful adoption of the specified pet.

4. Test Search Pet:
   - Purpose: Ensure that the search functionality works correctly for finding pets by name.
   - Method: test_search_pet
   - Assertion: Confirms that the search results contain at least one pet matching the search criteria and verifies that the pet's name is included in the results.

5. Test Adopt Non-Existent Pet:
   - Purpose: Test the system's response when trying to adopt a pet that does not exist.
   - Method: test_adopt_non_existent_pet
   - Assertion: Checks that the system raises a grpc.RpcError and verifies that the error status is NOT_FOUND with the appropriate error message.


## For Manually Running Docker

docker run -p 50051:50051 grpc-server

docker run -it --network="host" grpc-client



### Make sure you have the required software and libraries installed as mentioned in the prerequisites. Adjust the pet_id values in the test cases if you register new pets or adopt them during your testing. For Docker users, ensure that the Docker daemon is running.


## Acknowledgments

https://grpc.io/docs/ 
Postman : External tool for debug and test the scripts.
OpenAI and Perplexity for debugging and Testing and package upgrade and downgrade issues.










 