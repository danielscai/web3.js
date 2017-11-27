#!/usr/bin/env python3

import time
import asyncio
import websockets

async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print("< {}".format(name))

        greeting = "Hello {}!".format(name)
        await websocket.send(greeting)
        print("> {}".format(greeting))

async def hello2(websocket, path):
    #name = await websocket.recv()
    #print("< {}".format(name))
    name = 'hello'
    for i in range(1,10):
        greeting = "Hello {} {}!".format(name, i)
        await websocket.send(greeting)
        print("> {}".format(greeting))
        time.sleep(1)
    name = await websocket.recv()

start_server = websockets.serve(hello2, '', 8999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
