import asyncio

import www.orm
from www.Model import User, Blog, Comment


def test(loop):
    yield from www.orm.create_pool(loop=loop, user='erian', password='erian', db='blog')

    #u = User(name='Test4', email='test4@example.com', passwd='1234567890', image='about:blank')

    #yield from u.save()
    ulist = yield from User.findAll()
    for u in ulist:
        print(u)
    num = yield from User.findNumber()
    print('number is %s' % num)

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()