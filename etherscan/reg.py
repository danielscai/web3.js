#!/usr/bin/env python3

import time
import asyncio
import websockets

message = 0
connected = set()

async def consumer_handler(websocket, path):
    while True:
        message = await websocket.recv()
        await consumer(message)

async def consumer(message):
    global connected
    await asyncio.wait([ws.send(message) for ws in connected])

async def send_message():
    global connected
    global message
    while True:
        message +=1
        if connected:
            await asyncio.wait([ws.send('message {}'.format(message)) for ws in connected])
        await asyncio.sleep(1)

async def handlerReg(websocket, path):
    global connected
    # Register.
    print('connected {}'.format(websocket))
    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([websocket.send('hi')])
        await asyncio.wait([consumer_handler(websocket, path)])
    finally:
        # Unregister.
        print('removed {}'.format(websocket))
        connected.remove(websocket)


task1 = asyncio.ensure_future(send_message())
task2 = websockets.serve(handlerReg, '', 8999)

asyncio.get_event_loop().run_until_complete(task2)
asyncio.get_event_loop().run_forever()
