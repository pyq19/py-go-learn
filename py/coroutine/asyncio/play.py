import threading
import asyncio


async def hello():
    print('hello ! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('hello again ! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# hello ! (<_MainThread(MainThread, started 140737231500224)>)
# hello ! (<_MainThread(MainThread, started 140737231500224)>)
# hello again ! (<_MainThread(MainThread, started 140737231500224)>)
# hello again ! (<_MainThread(MainThread, started 140737231500224)>)
