#!/usr/bin/env python

from websockets.asyncio.client import connect
import argparse
import asyncio
import json
import os

async def main(args):
    prox = args.proxy
    if args.proxy == "":
        prox = os.getenv("CLOUDPROX_URL")

    async with connect(prox) as websocket:
        await websocket.send(json.dumps({
            "url": args.url,
            "method": args.method,
            "headers": {},
        }))

        content = await websocket.recv()
        print(f"{content}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('--proxy', '-p', default="")
    parser.add_argument('--method', '-X', default="GET")

    args = parser.parse_args()
    asyncio.run(main(args))
