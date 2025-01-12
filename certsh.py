#!/usr/bin/python3

ROCK ON!

import pycurl
import re
from io import BytesIO

DOMAIN = input("Enter domain: ")


curl = pycurl.Curl()
curl.setopt(curl.URL, f"https://crt.sh/?q={DOMAIN}")

buffer = BytesIO()
curl.setopt(curl.WRITEDATA, buffer)

curl.perform()
response = buffer.getvalue()
res = response.decode('utf-8')

regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'

domains = re.findall(regex, res)

uniq = set()

for domain in domains:
  if DOMAIN in domain:
    uniq.add(domain)

final = sorted(uniq)

for domain in final:
  print(domain)
