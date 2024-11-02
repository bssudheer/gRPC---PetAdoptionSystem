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

## For Manually Running Docker

docker run -p 50051:50051 grpc-server

docker run -it --network="host" grpc-client



### Make sure you have the required software and libraries installed as mentioned in the prerequisites. Adjust the pet_id values in the test cases if you register new pets or adopt them during your testing. For Docker users, ensure that the Docker daemon is running.


## Acknowledgments

https://grpc.io/docs/ 
Postman : External tool for debug and test the scripts.
OpenAI and Perplexity for debugging and Testing and package upgrade and downgrade issues.




