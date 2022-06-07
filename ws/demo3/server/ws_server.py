import asyncio
import json
import websockets
from _tweepy.Auth import TwitterAuth as TA


async def response(websocket, path):
    while True:
        try:
            app_client = TA.instance().app_client

            tweet_ids = [1460323737035677698]
            response = app_client.get_tweets(tweet_ids, tweet_fields=["created_at"])
            print(type(response.data))

            # message = await websocket.recv()
            # print(f"We got the message from the client: {message}")
        except websockets.ConnectionClosed:
            print('Terminated!')
            break

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
