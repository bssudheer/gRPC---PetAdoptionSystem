const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const readline = require('readline');

// Load the .proto file
const packageDefinition = protoLoader.loadSync('calculator.proto', {});
const calculatorProto = grpc.loadPackageDefinition(packageDefinition).calculator;

// Create gRPC client
const client = new calculatorProto.Calculator('localhost:50051', grpc.credentials.createInsecure());

// Create readline interface for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to ask the user for operation choice and numbers
function askOperation() {
    console.log("\n--- Calculator Menu ---");
    console.log("1: Add");
    console.log("2: Multiply");
    console.log("3: Exit");
    
    rl.question("Select an operation (1, 2, 3): ", function(choice) {
        if (choice === '1' || choice === '2') {
            rl.question("Enter the first number: ", function(num1) {
                rl.question("Enter the second number: ", function(num2) {
                    num1 = parseFloat(num1);
                    num2 = parseFloat(num2);

                    if (isNaN(num1) || isNaN(num2)) {
                        console.log("Please enter valid numbers.");
                        askOperation();  // Re-prompt if input is invalid
                        return;
                    }

                    if (choice === '1') {
                        // Call Add RPC
                        client.Add({ num1, num2 }, (error, response) => {
                            if (!error) {
                                console.log(`Result of ${num1} + ${num2} = ${response.result}`);
                            } else {
                                console.error("Error: ", error.message);
                            }
                            askOperation();  // Continue prompting after result
                        });
                    } else if (choice === '2') {
                        // Call Multiply RPC
                        client.Multiply({ num1, num2 }, (error, response) => {
                            if (!error) {
                                console.log(`Result of ${num1} * ${num2} = ${response.result}`);
                            } else {
                                console.error("Error: ", error.message);
                            }
                            askOperation();  // Continue prompting after result
                        });
                    }
                });
            });
        } else if (choice === '3') {
            console.log("Exiting...");
            rl.close();  // Exit the program
        } else {
            console.log("Invalid choice, please select 1, 2, or 3.");
            askOperation();  // Re-prompt if input is invalid
        }
    });
}

// Start the client interaction
askOperation();
