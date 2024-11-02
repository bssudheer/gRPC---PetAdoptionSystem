const { parentPort, workerData } = require('worker_threads');

const { task, petData, pets, petId } = workerData;

console.log(`Worker started for task: ${task}`);

const handleRequest = () => {
  let response;

  switch (task) {
    case 'register':
      petData.id = pets.length + 1; // Assign a new ID based on current length
      pets.push(petData); // Store the new pet
      response = { message: `Pet ${petData.name} has been registered.`, pets };
      break;

    case 'adopt':
      const petIndex = pets.findIndex(p => p.id === petId); // Find pet by ID
      if (petIndex === -1) {
        response = { error: true, message: 'Pet not found.' }; // Handle not found
      } else {
        const adoptedPet = pets.splice(petIndex, 1)[0]; // Remove the adopted pet
        response = { message: `Successfully adopted pet with ID: ${adoptedPet.id}`, pets };
      }
      break;

    case 'search':
      const foundPets = pets.filter(p =>
        (!petData.name || p.name.toLowerCase() === petData.name.toLowerCase()) &&
        (!petData.gender || p.gender.toLowerCase() === petData.gender.toLowerCase()) && // Updated to include gender
        (!petData.breed || p.breed.toLowerCase() === petData.breed.toLowerCase()) && // Updated to include breed
        (!petData.age || p.age === petData.age) &&
        (!petData.location || p.location.toLowerCase() === petData.location.toLowerCase()) // Updated to include location
      );

      response = { pets: foundPets, message: foundPets.length ? '' : 'No pets found.' };
      break;

    default:
      response = { error: true, message: 'Invalid task.' };
      break;
  }

  // Log when the worker finishes
  console.log(`Worker finished task: ${task}`);

  parentPort.postMessage(response);
};

handleRequest();
