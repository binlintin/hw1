import random
import requests
import sys

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: $ python3 request4statapp.py <number_of_integers>")
    sys.exit(1)  # Exit if the required argument isn't provided

try:
    # The number of random integers to generate, as provided by the command-line
    num_integers = int(sys.argv[1])
except ValueError:
    print("Please provide an integer value for the number of random integers.")
    sys.exit(1)  # Exit if the argument is not an integer

# User-Agent header to simulate a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

# The URL to the statistics application
URL = "https://db4.us/tech136/statapp.html"
r = requests.get(URL, headers=headers)
print(r)
print(r.content)

# Generate the random integers
random_integers = [random.randint(0, 100) for _ in range(num_integers)]
# Convert the list of integers to a string, joined by '%2C' which is URL encoded for ','
random_integers_str = '%2C'.join(map(str, random_integers))

# Make a request to the statistics application with the generated random integers
statapp_url = f"https://db4.us/cgi-bin/statapp.py?scores={random_integers_str}"
r = requests.get(statapp_url, headers=headers)
print(r)
print(r.content)
