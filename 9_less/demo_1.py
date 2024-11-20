import asyncio
from loguru import logger
from time import sleep

def foo_sync():
    logger.info("foo_sync start")
    sleep(.1)
    logger.info("foo_sync finish")

def bar_sync():
    logger.info("bar_sync start")
    sleep(.1)
    logger.info("bar_sync finish")
    
def run_sync():
    logger.info("Start sync")
    foo_sync()
    bar_sync()
    
    
async def foo():
    logger.info("async foo starting")
    await asyncio.sleep(1)
    logger.info("async foo finishing")
  
async def bar():
    logger.info("async bar starting")
    await asyncio.sleep(1)
    logger.info("async bar finishing")


async def run_async():
    await foo()
    await bar()
    
def run_main_async():
    logger.info("Starting main")
    #loop = asyncio.get_event_loop()
    #asyncio.run(run_async())
    
    coros=[
        foo(),
        bar(),
    ]
    
    fut = asyncio.wait(coros)
    print("fut", fut)
    asyncio.run(fut)
    logger.info("finishing main")
    
if __name__ == '__main__':
    #run_sync()
    run_main_async()