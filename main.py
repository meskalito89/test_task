"""! @brief This is test project for my new job."""


from os import path
from pdb import set_trace
import asyncio
from time import sleep
import aiohttp
from aiohttp.client_exceptions import ServerDisconnectedError

## configuration template
config_template = """IS_START=0"""


def it_is_first_run(config_path) -> bool:
    """function that check if script runing first time (by checking if config file allrady exists)."""
    if path.exists(config_path):
        return False
    return True

def is_start(config_path: str) -> int:
    """retrun IS_START flag from config file"""
    with open(config_path) as config_file:
        IS_START = config_file.readline().split('=')[-1]
        return int(IS_START)

def create_config_file(config_path: str) -> None:
    """
    Creates new config file

    @type  config_path:  str 
    @param config_path:  path to config file.
    """
    with open(config_path, 'w') as config_file:
        config_file.write(config_template)

def set_config(config_path: str) -> None:
    """
    Set flag IS_START in configuration file to 1

    @type  config_path:  str 
    @param config_path:  path to config file.
    """
    with open(config_path, 'w') as config_file:
        config_file.write("IS_START=1")
        

async def create_request(session: aiohttp.ClientSession, url: str) -> str:
    """
    Send one request 

    @param url: url address for request
    @param session: ClientSession 

    """
    while True:
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    print(f'ERROR: url {url}, status code {response.status}')
                    sleep(1)
                    continue
                response_json = await response.json()
                print(response_json)
                return response_json
        except  ServerDisconnectedError:
            continue


async def create_async_requests():
    """
    Function send asyncronious requests on urls:
        "http://localhost:3000/posts",
        "http://localhost:3000/profile",
        "http://localhost:3000/comments",
        "http://localhost:3000/public_data",
        "http://localhost:3000/danger_data",
    """

    urls = (
        "localhost:3000/posts",
        "localhost:3000/profile",
        "localhost:3000/comments",
        "localhost:3000/public_data",
        "localhost:3000/danger_data",
    )

    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            url = f'http://{url}'
            tasks.append(asyncio.ensure_future(create_request(session, url)))
        await asyncio.gather(*tasks)


def main():
    """
    After the first launch of the application, a configuration file with the IS_START=0 flag is created.
    If the IS_START flag is 0, then the application offers to set it to 1, depending on user input, or does not set this flag, after which it restarts.
    If the IS_START flag is 1, then go to the next step

    The application starts working and requests 5 different requests from the server (we will provide the server with data and access description).
    After the responses for all requests are received, the application should print the responses from the requests in plain text to the console

    After all requests have been processed, the application displays the text "Job completed" and leaves the console window open.
    We consider that the work of the application is over.
    """
    while True:
        config_path = 'config'
        if it_is_first_run(config_path):
            create_config_file(config_path)

        if not is_start(config_path):
            if input("Set IS_START variable to 1? (yes/no): ") == "yes":
                set_config(config_path)
            continue
        else:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(create_async_requests())

            break

    print("The work is done")
    input()

if __name__ == "__main__":
    main()

