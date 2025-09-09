#!/usr/bin/env python3

import asyncio

try:
    import websockets
except ImportError:
    websockets = None

async def echo(ws, path):
    """Simple echo handler for WebSocket connections."""
    async for message in ws:
        await ws.send(message)

def start_server(host='localhost', port=8765):
    """Start a WebSocket server if the websockets library is available."""
    if websockets is None:
        raise RuntimeError("websockets library is not installed")
    loop = asyncio.get_event_loop()
    server = websockets.serve(echo, host, port)
    loop.run_until_complete(server)
    loop.run_forever()

if __name__ == '__main__':
    start_server()
