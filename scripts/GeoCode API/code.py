import urllib.request
import urllib.parse
import urllib.error
import json
import os
import webbrowser
import ssl
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['keys']['api_key']
service_url = config['keys']['service_url']

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open("where.txt") as fh, open("where.js", "w", encoding="utf-8") as where:
    adrs = []
    parms = {}
    for line in fh:

        address = line.strip()
        parms["address"] = address
        parms['key'] = api_key
        url = service_url + urllib.parse.urlencode(parms)

        if url.lower().startswith('http'):
            req = urllib.request.Request(url)
        else:
            raise ValueError from None

        with urllib.request.urlopen(req, context=ctx) as resp:

            data = resp.read().decode()

            try:
                js = json.loads(data)
            except Exception as e:
                print(f"{e}: {data}")
                continue

            try:
                adrs.append([js['results'][0]['geometry']['lat'],
                             js['results'][0]['geometry']['lng'],
                             js['results'][0]['formatted']])
                print('Retrieved ', url)
            except Exception as e:
                print(f"Not Found: {e}: {line.strip()}")

    print("\nOpening Webpage")

    where.write("myData = [\n")
    for item in adrs:
        where.write(f"[{str(item[0])}, {str(item[1])}, '{str(item[2])}' ], \n")
    where.write("];\n")

webbrowser.open('file://' + os.path.realpath("index.html"))
