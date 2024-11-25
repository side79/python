import asyncio
from asyncio import CancelledError
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger

@dataclass
class Service:
    name: str
    url: str
    ip_field: str
    
SERVICES = [
    Service("ipify","https://api64.ipify.org/?format=json", "ip"),
    Service("ip-api","http://ip-api.com/json", "query"),
]

async def fetch(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()
    

async def fetch_ip(service: Service) -> str:
   
    async with ClientSession() as session:
        result = await fetch(session, service.url)
    logger.info("Got result for {}, result {}", service.name, result)
    return  result[service.ip_field]

async def get_my_ip():
    cors = [asyncio.create_task(fetch_ip(s)) for s in SERVICES]
    done, pading = await asyncio.wait(
        cors,
        timeout=3,
        return_when=asyncio.FIRST_COMPLETED
    )
    
    for t in pading:
        t.cancel()
        
    my_ip = None
    
    for t in done:
        my_ip = t.result()
        break
    else:
        logger.warning("No result")
        
    logger.info("Got my ip {}", my_ip)


def run_main():
    asyncio.run(get_my_ip())
        
if __name__ == "__main__":
    run_main()