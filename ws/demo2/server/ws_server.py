import asyncio
import websockets

async def response(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            print(f"We got the message from the client: {message}")
        except websockets.ConnectionClosed:
            print('Terminated!')
            break

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
