import requests
from pprint import pprint
# 702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d

main_link = 'https://api.github.com'
token = '702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d'
params = {'Authorization': token}
response = requests.get(main_link, params)

pprint(response)
print(1)
