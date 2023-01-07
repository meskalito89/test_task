import asyncio
import aiohttp
import requests
from pdb import set_trace
import time


start_time = time.time()

urls = (
    "http://localhost:3000/posts",
    "http://localhost:3000/profile",
    "http://localhost:3000/comments",
    "http://localhost:3000/public_data",
    "http://localhost:3000/danger_data",
)

for url in urls:
    response = requests.get(url)
    print(response.text)




print(time.time() - start_time)