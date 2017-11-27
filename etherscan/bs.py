#!/usr/bin/env python3

import json
import asyncio
import datetime
import random
import websockets

async def crawl():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    rdata = { "betid":"hello","player":"world","now":now}
    return json.dumps(rdata)

async def time(websocket, path):
    while True:
        now = await crawl()
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '', 8999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

