import requests
import time

# Define the URL you want to call
url = 'https://suntechnoconsulting.online'

# Define the number of iterations and the delay between requests
num_iterations = 100
delay = 1  # seconds

for i in range(num_iterations):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Print the status code and response text
        print(f'Iteration {i + 1}: Status Code: {response.status_code}')
        print(response.text[:200])  # Print first 200 characters of the response text
        
    except requests.RequestException as e:
        # Print any exceptions that occur
        print(f'Iteration {i + 1}: An error occurred: {e}')
    
    # Wait for the specified delay before the next request
    #time.sleep(delay)