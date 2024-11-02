import grpc
import pet_adoption_pb2
import pet_adoption_pb2_grpc

def register_pet(stub):
    name = input("Enter the pet's name: ")
    gender = input("Enter the pet's gender (e.g., Male, Female): ")  # New input
    breed = input("Enter the pet's breed: ")  # New input
    age = int(input("Enter the pet's age: "))
    location = input("Enter the pet's location: ")  # New input
    pet = pet_adoption_pb2.Pet(name=name, gender=gender, breed=breed, age=age, location=location)  # Updated
    response = stub.RegisterPet(pet)
    print(f"Pet {name} has been registered.")

def fetch_pets(stub):
    print("Fetching list of pets:")
    response = stub.GetPets(pet_adoption_pb2.Empty())
    
    if not response.pets:  # Check if the list is empty
        print("No pets available.")
    else:
        for pet in response.pets:
            print(f"Pet ID: {pet.id}, Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}, Location: {pet.location}")

def adopt_pet(stub):
    pet_id = int(input("Enter the ID of the pet you want to adopt: "))
    try:
        adopt_response = stub.AdoptPet(pet_adoption_pb2.PetIdRequest(petId=pet_id))
        print(adopt_response.message)
    except grpc.RpcError as e:
        print(f"Error: {e.details()}")  # Print the error message returned by the server

def search_pet(stub):
    search_name = input("Enter a name to search for pets: ")
    search_response = stub.SearchPets(pet_adoption_pb2.PetSearchRequest(name=search_name))
    
    if not search_response.pets:
        print("No pets found matching the search criteria.")
    else:
        print("Search Results:")
        for pet in search_response.pets:
            print(f"Pet ID: {pet.id}, Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}, Location: {pet.location}")

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pet_adoption_pb2_grpc.PetAdoptionStub(channel)

        while True:
            print("\nMenu:")
            print("1. Register a new pet")
            print("2. Fetch list of pets")
            print("3. Adopt a pet")
            print("4. Search for a pet")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                register_pet(stub)
            elif choice == '2':
                fetch_pets(stub)
            elif choice == '3':
                adopt_pet(stub)
            elif choice == '4':
                search_pet(stub)
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
