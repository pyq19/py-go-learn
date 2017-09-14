# coding:utf8
# https://docs.python.org/3/library/asyncio-task.html


import asyncio


async def compute(x, y):
    print('compute %s + %s ...' % (x, y))
    await asyncio.sleep(2)
    return x + y


async def print_sum(x, y):
    print('begin !')
    result = await compute(x, y)
    print(f'result ->{result}')


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()

# begin !
# compute 1 + 2 ...
# result ->3
