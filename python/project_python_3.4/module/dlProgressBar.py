"""
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.6 get-pip.py requests --target .
python3.6 get-pip.py tqdm --target .
"""
from tqdm import tqdm
import requests
import math


proxies = {
  "http": None,
  "https": None,
}

url = " http://192.168.XXX.XXX:20XXX/XXXX/OVA/RHEL7.5/demo.installer75_candidate_v1.ova"
# Streaming, so we can iterate over the response.
r = requests.get(url, stream=True, proxies=proxies)

# Total size in bytes.
total_size = int(r.headers.get('content-length', 0)); 
block_size = 1024
wrote = 0 
with open('output.bin', 'wb') as f:
    for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
        wrote = wrote  + len(data)
        f.write(data)
if total_size != 0 and wrote != total_size:
    print("ERROR, something went wrong") 
