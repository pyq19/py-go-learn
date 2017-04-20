# before 3.5

import asyncio


@asyncio.coroutine
def slow_operation(n):
    yield from asyncio.sleep(1)
    print('slow operation {} complete'.format(n))

@asyncio.coroutine
def main():
    yield from asyncio.wait([
        slow_operation(1),
        slow_operation(2),
        slow_operation(3),
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# slow operation 2 complete
# slow operation 1 complete
# slow operation 3 complete
