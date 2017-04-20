# 3


import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('DONE!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
print('Future DONE ->', future.done())
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print('Future DONE ->', future.done())
print(future.result())
loop.close()
# Future DONE -> False
# Future DONE -> True
# DONE!
