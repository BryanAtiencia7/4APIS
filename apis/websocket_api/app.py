import asyncio
import websockets

async def hello(websocket, path):
    await websocket.send("Hello World from WebSocket API!")

start_server = websockets.serve(hello, "0.0.0.0", 5004)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
