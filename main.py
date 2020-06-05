import requests
from pprint import pprint
# 702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d
# https://api.github.com/search/repositories?q=
enter_link = 'https://api.github.com'
repo_link = 'https://api.github.com/search/repositories'
token = '702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d'

params = {'Authorization':token,
          'q':'user:valdei777'}
response = requests.get(repo_link, params=params)

pprint(response.text)
print(1)
