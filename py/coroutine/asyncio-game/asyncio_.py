# 3.5

# https://7webpages.com/blog/writing-online-multiplayer-game-with-python-asyncio-getting-asynchronous/

import asyncio

async def my_task(seconds):
    print('start sleeping for {} seconds.'.format(seconds))
    await asyncio.sleep(seconds)
    print('end sleeping for {} seconds.'.format(seconds))

all_tasks = asyncio.gather(my_task(1), my_task(2))
loop = asyncio.get_event_loop()
loop.run_until_complete(all_tasks)
loop.close()
# start sleeping for 2 seconds.
# start sleeping for 1 seconds.
# end sleeping for 1 seconds.
# end sleeping for 2 seconds.
