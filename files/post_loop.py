import requests
import argparse

token_file = open('./token.txt')

token = str([line.rstrip('\n') for line in token_file][0])
parser = argparse.ArgumentParser()
parser.add_argument('--env', type=str, help="the environment", required=True)
args = parser.parse_args()

environment = args.env

host = 'https://organization-catalogue' + environment + 'fellesdatakatalog.digdir.no'
url = host + "/organizations"
# headers
get_headers = {'Content-Type': 'application/json'}
post_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

print("Getting to the following url: ", url)
r = requests.get(url, headers=get_headers)
body = r.json()

for organization in body:
    orgId = organization.get("organizationId")
    p = requests.post(url + "/" + str(orgId), headers=post_headers)
    print(str(p.status_code) + " : " + str(orgId))
