import asyncio
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

async def fetch_ip(service: Service) -> str:
    """_summary_

    Args:
        service (Service): _description_

    Returns:
        str: _description_
    """
    my_ip = "not found"