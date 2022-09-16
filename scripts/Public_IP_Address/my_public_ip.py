from urllib.request import urlopen

url = "http://checkip.dyndns.org"

print("Making request to " + url + "...")
request = urlopen(url)

print("Reading the response...")
response = request.read()

print("Extracting your IP info...")
ip = ">>> " + response.decode("utf-8").split("body")[1][1:-2] + " <<<"
print(ip)