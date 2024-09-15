import sys

def run(user_input):
    if user_input.strip() == "exit":  # Exit condition
        return "Exiting the test script."
    
    response = f"Received: {user_input.strip()}"  # Prepare the response
    return response  # Return the response