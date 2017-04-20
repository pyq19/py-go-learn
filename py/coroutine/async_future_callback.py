from functools import partial
import asyncio


def set_result(future, result):
    print('setting future result to {!r}'.format(result)) # !!!{!r}
    future.set_result(result)

def callback(who, future):
    print('[{}]: returned result: {!r}'.format(who, future.result()))


event_loop = asyncio.get_event_loop()
future = asyncio.Future()
future.add_done_callback(partial(callback, 'CB1'))
event_loop.call_soon(set_result, future, 'Done....')
future.add_done_callback(partial(callback, 'CB2'))
event_loop.run_until_complete(future)
event_loop.close()
# setting future result to 'Done....'
# [CB1]: returned result: 'Done....'
# [CB2]: returned result: 'Done....'
