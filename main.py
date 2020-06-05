import requests
import pprint
# 702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d

main_link = 'https://api.github.com/graphql'
token = '702a9c45c5c1c4d8ca215af4db70ee75dd5fff3d'
coll = {'user': token,
'repo':'status',
'read':'repo_hook',
'read':'org',
'read':'public_key',
'read':'gpg_key'}
response = requests.get(main_link, coll)

pprint(respons)
print(1)