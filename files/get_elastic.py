import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, help="host", required=True)
parser.add_argument('--index', type=str, help="elastic index", required=True)
parser.add_argument('--env', type=str, help="the environment", required=True)
args = parser.parse_args()

host = args.host
cookieName = ''
cookieValue = ''
cookies = {cookieName: cookieValue}
url = args.host + args.index + '/_search'
prod_url = 'https://data.norge.no/publisher'
data = json.loads('{"query":{"bool":{"must":[{"wildcard":{"name":"*"}}],"must_not":[],"should":[]}},"from":0,"size":1000,"sort":[],"aggs":{}}')
headers = {'Content-Type': 'application/json'}

if args.env == "prod":
    r = requests.get(prod_url)
else:
    print("Posting to url: " + url)
    r = requests.post(url, cookies=cookies, json=data, headers=headers)

with open('./tmp/' + 'elastic_' + args.env + '.json', 'w', encoding="utf-8") as outfile:
    json.dump(r.json(), outfile, ensure_ascii=False, indent=4)


