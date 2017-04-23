import json
import threading
import time
import unittest
import urlparse
import uuid     # !!!


def check_token(conn, token):
    return conn.hget('login:', token)


def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)


QUIT = False
LIMIT = 10000000

def clean_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time.sleep(1)
            continue
        
        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange('recent:', 0, end_index-1)

        session_keys = []
        for token in tokens:
            session_keys.append('viewed:' + token)

        # remove the oldest tokens
        conn.delete(*session_keys)
        conn.hdel('login:', *tokens)
        conn.zrem('recent:', *tokens)


def add_to_cart(conn, session, item, count):
    if count <= 0:
        conn.hrem('cart:' + session, item) # remove the item from the cart
    else:
        conn.hset('cart:' + session, item, count) # add the item to the cart


def clean_full_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time.sleep(1)
            continue
        
        end_index = min(size - LIMIT, 100)
        sessions = conn.zrange('recent:', 0, end_index-1)

        session_keys = []
        for sess in sessions:
            session_keys.append('viewed:' + sess)
            session_keys.append('cart:' + sess)

        conn.delete(*session_keys)
        conn.hdel('login:', *sessions)
        conn.zrem('recent:', *sessions)


def cache_request(conn, request, callback):
    if not can_cache(conn, request):
        return callback(request)

    page_key = 'cache:' + hash_request(request)
    content = conn.get(page_key)

    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)

    return content


def schedule_row_cache(conn, row_id, delay):
    conn.zadd('delay:', row_id, delay)
    conn.zadd('schedule:', row_id, time.time())


def cache_rows(conn):
    while not QUIT:
        next = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()
        if not next or next[0][1] > now:
            time.sleep(.05)
            continue

        row_id = next[0][0]
        delay = conn.zscore('delay:', row_id)
        if delay <= 0:
            conn.zrem('delay:', row_id)
            conn.zrem('schedule:', row_id)
            conn.delete('inv:' + row_id)
            continue

        row = Inventory.get(row_id)
        conn.zadd('schedule:', row_id, now + delay)
        conn.set('inv:' + row_id, json.dumps(row.to_dict()))


def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)
        conn.zincrby('viewed:', item, -1)


def rescale_viewed(conn):
    while not QUIT:
        conn.zremrangebyrank('viewed:', 0, -20001)
        conn.zinterstore('viewed:', {'viewed:': .5})
        time.sleep(300)


def can_cache(conn, request):
    item_id = extract_item_id(request)
    if not item_id or is_dynamic(request):
        return False
    rank = conn.zrank('viewed:', item_id)
    return rank is not None and rank < 10000


###### below this line are helpers to test the code


def extract_item_id(request):
    parsed = urlparse.urlparse(request)
    query = urlparse.parse_qs(parsed.query)
    return (query.get('item') or [None])[0]

def is_dynamic(request):
    parsed = urlparse.urlparse(request)
    query = urlparse.parse_qs(parsed.query)
    return '_' in query

def hash_request(request):
    return str(hash(request))


class Inventory(object):
    def __init__(self, id):
        self.id = id

    @classmethod
    def get(cls, id):
        return Inventory(id)

    def to_dict(self):
        return {'id':self.id, 'data':'data to cache...', 'cached':time.time()}


class TestCh02(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(db=15)

    def tearDown(self):
        conn = self.conn
        to_del = (
            conn.keys('login:*') + conn.keys('recent:*') + 
            conn.keys('viewed:*') + conn.keys('cart:*') + 
            conn.keys('cache:*') + conn.keys('delay:*') +
            conn.keys('schedule:*') + conn.keys('inv:*')
        )
        if to_del:
            self.conn.delete(*to_del)
        del self.conn
        global QUIT, LIMIT
        QUIT = False
        LIMIT = 10000000
        print
        print

    def test_login_cookies(self):
        conn = self.conn
        global LIMIT, QUIT
        token = str(uuid.uuid4())

        update_token(conn, token, 'username', 'itemX')
        print 'we just logged-in/updated token ->', token
        print 'for user:', 'username'
        print

        print 'what username do we get when we look-up that token ?'
        r = check_token(conn, token)
        print r
        print 
        self.assertTrue(r)

        print 'lets drop the maximum number of cookies to 0 to clean them out'
        print 'we will start a thread to do the cleaning, while we stop it later'
        LIMIT = 0
        t = threading.Thread(target=clean_sessions, args=(conn,))
        t.setDaemon(1) # to make sure it dies if we ctrl+c quit
        t.start()
        time.sleep(1)
        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception('the clean sessions thread is still alive?!')

        s = conn.hlen('login:')
        print 'the current number of sessions still available is ->', s
        self.assertFalse(s)
    
    def test_shopping_cart_cookies(self):
        conn = self.conn
        global LIMIT, QUIT
        token = str(uuid.uuid4())

        print 'we will refresh our session...'
        update_token(conn, token, 'username', 'itemX')
        print 'and add an item to the shopping cart'
        add_to_cart(conn, token, 'itemY', 3)
        r = conn.hgetall('cart:' + token)
        print 'our shopping cart currently has ->', r
        print

        self.assertTrue(len(r) >= 1)

        print 'lets clean out our sessions and carts'
        LIMIT = 0
        t = threading.Thread(target=clean_full_sessions, args=(conn,))
        t.setDaemon(1)
        t.start()
        time.sleep(1)
        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception('the clean sessions thread is still alive?!')

        r = conn.hgetall('cart:' + token)
        print 'our shopping cart now contains ->', r

        self.assertFalse(r)

    def test_cache_request(self):
        conn = self.conn
        token = str(uuid.uuid4())

        def callback(request):
            return 'content for ->' + request

        update_token(conn, token, 'username', 'itemX')
        url = 'http://test.com/?item=itemX'
        print 'we are going to cache a simple request against ->', url
        result = cache_request(conn, url, callback)
        print 'we got install content ->', repr(result)
        print

        self.assertTrue(result)

        print 'to test that we have cache the request, we will pass a bad callback'
        result2 = cache_request(conn, url, None)
        print 'we ended up getting the same response! ->', repr(result2)

        self.assertEquals(result, result2)

        self.assertFalse(can_cache(conn, 'http://test.com/'))
        self.assertFalse(can_cache(conn, 'http://test.com/?item=itemX&_=123456'))

    def test_cache_rows(self):
        import pprint
        conn = self.conn
        global QUIT

        print 'first, let us schedule caching of itemX every 5s'
        schedule_row_cache(conn, 'itemX', 5)
        print 'our schedule looks like ->'
        s = conn.zrange('schedule:', 0, -1, withscores=True)
        pprint.pprint(s)
        self.assertTrue(s)

        print 'we wiil start a caching thread that will cache the data...'
        t = threading.Thread(target=cache_rows, args=(conn,))
        t.setDaemon(1)
        t.start()

        time.sleep(1)
        print 'our cached data look like->'
        r = conn.get('inv:itemX')
        print repr(r)
        self.assertTrue(r)
        print
        print 'we will check again in 5s...'
        time.sleep(5)
        print 'notice that the data has changed....'
        r2 = conn.get('inv:itemX')
        print repr(r2)
        print
        self.assertTrue(r2)
        self.assertTrue(r != r2)

        print 'lets force un-caching'
        schedule_row_cache(conn, 'itemX', -1)
        time.sleep(1)
        r = conn.get('inv:itemX')
        print 'the cache was cleared? ->', not t
        print 
        self.assertFalse(r)

        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception('the database caching thread is still alive???')


if __name__ == '__main__':
    unittest.main()

