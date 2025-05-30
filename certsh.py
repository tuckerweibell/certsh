#!/usr/bin/python3

import pycurl
import re
import sys
from io import BytesIO

if len(sys.argv) < 2:
    print("Usage: certsh <domain>")
    sys.exit(1)

DOMAIN = sys.argv[1]

curl = pycurl.Curl()
curl.setopt(curl.URL, f"https://crt.sh/?q={DOMAIN}")

buffer = BytesIO()
curl.setopt(curl.WRITEDATA, buffer)

curl.perform()
curl.close()

response = buffer.getvalue().decode('utf-8')

regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
domains = re.findall(regex, response)

uniq = set()

for domain in domains:
    if DOMAIN in domain:
        uniq.add(domain)

final = sorted(uniq)

for domain in final:
    print(domain)
