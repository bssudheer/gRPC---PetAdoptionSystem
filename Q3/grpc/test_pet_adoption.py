import grpc
import unittest
import pet_adoption_pb2
import pet_adoption_pb2_grpc

class TestPetAdoptionSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.channel = grpc.insecure_channel('localhost:50051')
        cls.stub = pet_adoption_pb2_grpc.PetAdoptionStub(cls.channel)

    def test_register_pet(self):
        pet = pet_adoption_pb2.Pet(name='Buddy', gender='Male', age=3, breed='Golden Retriever', location='Dallas')
        response = self.stub.RegisterPet(pet)
        self.assertEqual(response.message, 'Pet Buddy has been registered.')  # Adjust based on actual message from server

    def test_fetch_pets(self):
        new_pet = pet_adoption_pb2.Pet(name="Buddy", gender='Male', age=3, breed='Golden Retriever', location='Dallas')
        self.stub.RegisterPet(new_pet)

        response = self.stub.GetPets(pet_adoption_pb2.Empty())
        self.assertTrue(len(response.pets) > 0, "Expected pets to be available.")

    def test_adopt_pet(self):
        pet = pet_adoption_pb2.Pet(name='Buddy', gender='Male', age=3, breed='Golden Retriever', location='Dallas')
        self.stub.RegisterPet(pet)  # Register the pet to ensure it exists
        
        pet_id = 1  # Assuming the first registered pet has ID 1
        adopt_response = self.stub.AdoptPet(pet_adoption_pb2.PetIdRequest(petId=pet_id))
        self.assertEqual(adopt_response.message, f"Successfully adopted pet with ID: {pet_id}")  # Adjusted message

    def test_search_pet(self):
        search_name = 'Buddy'
        search_response = self.stub.SearchPets(pet_adoption_pb2.PetSearchRequest(name=search_name))
        self.assertTrue(len(search_response.pets) > 0, "Expected at least one pet to match the search criteria.")

    def test_adopt_non_existent_pet(self):
        non_existent_pet_id = 999  # Assuming this ID does not exist in the system
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.AdoptPet(pet_adoption_pb2.PetIdRequest(petId=non_existent_pet_id))
        
        # Check if the error status is NOT_FOUND
        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)
        self.assertEqual(context.exception.details(), "Pet not found.")

    @classmethod
    def tearDownClass(cls):
        cls.channel.close()

if __name__ == "__main__":
    unittest.main()
