import json
import requests
import argparse

token_file = open('./token.txt')

token = str([line.rstrip('\n') for line in token_file][0])
parser = argparse.ArgumentParser()
parser.add_argument('--env', type=str, help="the environment", required=True)
args = parser.parse_args()
environment = args.env
elastic_file = './tmp/elastic_' + environment.replace('.', '') + '.json'

if environment == "prod":
    environment = "'"

host = 'https://organization-catalogue' + environment + 'fellesdatakatalog.digdir.no'
url = host + "/organizations"
# headers
put_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

print("Putting to the following url: ", url)
# Load the publisher by posting the data:
with open(elastic_file) as input_file:
    for publisher in json.load(input_file)["hits"]["hits"]:
        orgId = publisher["_source"].get("id")
        g = requests.get(url + "/" + str(orgId))
        prefLabelElastic = publisher["_source"].get("prefLabel")
        if prefLabelElastic:
            prefLabel = {}
            if prefLabelElastic.get("no"):
                prefLabel["nb"] = prefLabelElastic.get("no")
            if prefLabelElastic.get("nb"):
                prefLabel["nb"] = prefLabelElastic.get("nb")
            if prefLabelElastic.get("nn"):
                prefLabel["nn"] = prefLabelElastic.get("nn")
            if prefLabelElastic.get("en"):
                prefLabel["en"] = prefLabelElastic.get("en")
            if len(prefLabel) > 0:
                body = {'prefLabel': prefLabel}

                p = requests.put(url + "/" + str(orgId), headers=put_headers, json=body)
                print(str(p.status_code) + " : " + str(orgId))
