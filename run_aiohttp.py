import asyncio
import random

import ujson
import uvloop
from aiohttp import web
from shared import setup_db


async def startup(app):
    app['db'] = await setup_db(app.loop)


async def cleanup(app):
    await app['db'].close()


async def index(request):
    data = {'message': 'hello world'}
    body = ujson.dumps(data)
    return web.Response(body=body.encode(), content_type='application/json')


async def db(request):
    user_id = random.randrange(1, 1000)
    async with request.app['db'].acquire() as conn:
        username = await conn.fetchval('SELECT name from users WHERE id=$1', user_id)
    data = {'message': f'hello {username}'}
    body = ujson.dumps(data)
    return web.Response(body=body.encode(), content_type='application/json')


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = web.Application()
app.on_startup.append(startup)
app.on_cleanup.append(cleanup)
app.router.add_get('/', index)
app.router.add_get('/db', db)

web.run_app(app, port=8000, access_log=None)
