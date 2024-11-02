const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync('calculator.proto', {});
const calculatorProto = grpc.loadPackageDefinition(packageDefinition).calculator;

// Implement the Calculator service
function add(call, callback) {
  callback(null, { result: call.request.num1 + call.request.num2 });
}

function multiply(call, callback) {
  callback(null, { result: call.request.num1 * call.request.num2 });
}

// Start the server
function main() {
  const server = new grpc.Server();
  server.addService(calculatorProto.Calculator.service, { Add: add, Multiply: multiply });
  server.bindAsync('127.0.0.1:50051', grpc.ServerCredentials.createInsecure(), () => {
    console.log('Node.js gRPC server running...');
    server.start();
  });
}

main();
