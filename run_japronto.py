import random

import ujson
from japronto import Application
from shared import setup_db


def index(request):
    data = {'message': 'hello world'}
    body = ujson.dumps(data)
    return request.Response(text=body)


async def db(request):
    user_id = random.randrange(1, 1000)
    async with request.app.db.acquire() as conn:
        username = await conn.fetchval('SELECT name from users WHERE id=$1', user_id)
    data = {'message': f'hello {username}'}
    body = ujson.dumps(data)
    return request.Response(text=body, headers={'Content-Type': 'application/json'})


app = Application()
app.db = app.loop.run_until_complete(setup_db(app.loop))
app.router.add_route('/', index)
app.router.add_route('/db', db)
app.run(port=8000)  # worker_num=2 works for index but not db
