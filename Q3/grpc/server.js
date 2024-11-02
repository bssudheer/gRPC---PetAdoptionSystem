const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');
const { Worker } = require('worker_threads');

const PROTO_PATH = path.join(__dirname, 'pet_adoption.proto');

// Load the protobuf
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {});
const petAdoptionProto = grpc.loadPackageDefinition(packageDefinition);

// Sample data
let pets = [];

// Utility function to handle worker creation
const createWorker = (task, petData = {}, petId = null, callback) => {
  const worker = new Worker(path.join(__dirname, 'worker.js'), {
    workerData: { task, petData, pets, petId },
  });

  worker.on('message', (response) => {
    if (response.error) {
      callback({
        code: grpc.status.NOT_FOUND,
        details: response.message,
      });
    } else {
      pets = response.pets; // Update pets after operation
      callback(null, { message: response.message, pets: response.pets });
    }
  });

  worker.on('error', (error) => {
    console.error('Worker error:', error);
    callback({
      code: grpc.status.INTERNAL,
      details: 'An internal error occurred',
    });
  });
};

// Define the service methods
const getPets = (call, callback) => {
  callback(null, { pets });
};

const adoptPet = (call, callback) => {
  const petId = call.request.petId;
  createWorker('adopt', {}, petId, callback);
};

const registerPet = (call, callback) => {
  const newPet = call.request;
  createWorker('register', newPet, null, callback);
};

const searchPets = (call, callback) => {
  const searchCriteria = call.request;
  createWorker('search', searchCriteria, null, callback);
};

// Create the server
const server = new grpc.Server();
server.addService(petAdoptionProto.petAdoption.PetAdoption.service, {
  GetPets: getPets,
  AdoptPet: adoptPet,
  RegisterPet: registerPet,
  SearchPets: searchPets,
});

// Start the server using bindAsync
const PORT = '50051';
server.bindAsync(`0.0.0.0:${PORT}`, grpc.ServerCredentials.createInsecure(), (error, port) => {
  if (error) {
    console.error('Failed to bind server:', error);
    return;
  }
  console.log(`Server running at http://127.0.0.1:${port}`);
  server.start();
});
