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
    #while message != 0:
    while True:
    #if 1:
        message +=1
        print(connected)
        print("message {}".format(message))
        #a=[ws.send("message {}!".format(message)) for ws in connected]
        await asyncio.sleep(1)
        #await asyncio.wait([ws.send(str(message)) for ws in connected])
        #a=[ws.send("message {}!".format(message)) for ws in connected]
        #for ws in connected:
        #    ws.send("message {}!".format(message))
        await asyncio.wait([ws.send("message {}!".format(message)) for ws in connected])

def send_message2():
    global connected
    global message
    #while message != 0:
    while True:
    #if 1:
        message +=1
        print(connected)
        print("message {}".format(message))
        #a=[ws.send("message {}!".format(message)) for ws in connected]
        time.sleep(1)
        #a=[ws.send("message {}!".format(message)) for ws in connected]
        for ws in connected:
            ws.send("message {}!".format(message))
        #await asyncio.wait([ws.send("message {}!".format(message)) for ws in connected])
#task = asyncio.ensure_future(send_message())

async def mock(websocket,path):
    #send_message2()
    await asyncio.wait([send_message(),handlerReg(websocket,path)])
    #await handlerReg(websocket,path)
    #await send_message()


async def handlerReg(websocket, path):
    global connected
    # Register.
    print('connected {}'.format(websocket))
    connected.add(websocket)
    try:
        # Implement logic here.
        #while True:
        await asyncio.wait([websocket.send('hi')])
        await asyncio.wait([consumer_handler(websocket, path)])
        #await asyncio.wait([ws.send("world") for ws in connected])
    finally:
        # Unregister.
        print('removed {}'.format(websocket))
        connected.remove(websocket)


start_server = websockets.serve(mock, '', 8999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

