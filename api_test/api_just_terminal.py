#just show the response in the terminal (do this to get it working before sending to flask)

#pipenv install requests
#pipenv shell
#python convert.py (just to run this code, doesn't launch a server)

import requests
#no password
response = requests.get("https://aztro.sameerkumar.website/?sign=pisces&day=today")
#password
# response = requests.get(
#   'https://api.github.com/user', 
#   auth=HTTPBasicAuth('username', 'password')
# )

#print response code
print(response)

# Return the raw bytes of the data payload
print(response.content())

# Return a string representation of the data payload
print(response.text())

# This method is convenient when the API returns JSON
save_as_json_to_access_keys = response.json()
print(save_as_json_to_access_keys['description'])
