import requests
import random
import time

api_success = "http://localhost:32769/success"
api_failure = "http://localhost:32769/failure"

def make_random_request():
    # Generate a random number between 0 and 1
    random_number = random.random()

    if random_number < 0.9:
        response = requests.get(api_success)
        print("Success API - Response:", response.text)
    else:
        response = requests.get(api_failure)
        print("Failure API - Response:", response.text)

if __name__ == "__main__":
    while True:
        make_random_request()
        time.sleep(1)