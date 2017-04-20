import asyncio


async def log(msg):
    print(msg)


class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context......')

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context....')

async def coro():
    async with AsyncContextManager():
        print('body')

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
# entering context......
# body
# exiting context....


c = coro()
try:
    c.send(None)
except StopIteration:
    print('finished ....')
# entering context......
# body
# exiting context....
# finished ....
