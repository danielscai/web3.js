#!/usr/bin/env python3

import time
import asyncio
import websockets

connected = set()

async def consumer(message):
    print("get message {}".format(message))

async def producer():
    return "message produces"

async def consumer_handler(websocket, path):
    while True:
        message = await websocket.recv()
        await consumer(message)

async def consumer(message):
    global connected
    print(message)
    print(connected)
    await asyncio.wait([ws.send(message) for ws in connected])

async def producer_handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(message)

async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(producer_handler(websocket, path))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()

message = 0

async def send_message():
    global connected
    global message
    while True:
        message +=1
        print(connected)
        print("message {}".format(message))
        [ws.send('message:') for ws in connected]
        await asyncio.sleep(1)

async def handlerReg(websocket, path):
    global connected
    # Register.
    print('connected {}'.format(websocket))
    connected.add(websocket)
    print(id(connected))
    try:
        # Implement logic here.
        await asyncio.wait([websocket.send('hi')])
        await asyncio.wait([consumer_handler(websocket, path)])
    finally:
        # Unregister.
        print('removed {}'.format(websocket))
        connected.remove(websocket)



task1 = asyncio.ensure_future(send_message())
start_server = websockets.serve(handlerReg, '', 8999)
tasks = asyncio.wait([task1, start_server])

asyncio.get_event_loop().run_until_complete(tasks)
asyncio.get_event_loop().run_forever()
