from config import Config
from ticker import Ticker

import asyncio
import json
import websockets

ticker = Ticker()

async def updateTicker():
	while True:
		await asyncio.sleep(Config.updateRate)
		ticker.saveTickerFile()

async def startSocket():
	async with websockets.connect('ws://localhost:5672') as websocket:
		on_open()
		while True:
			message = await websocket.recv()
			on_message(message)

def on_message(message):
	obj = json.loads(message)
	channel = obj['channel']
	payload = obj['payload']


	if channel == "track":
		ticker.title  = payload['title']
		ticker.artist = payload['artist']
		ticker.album  = payload['album']
	elif channel == "playState":
		ticker.playing = payload

def on_open():
	print('Connected')

def main():
	Config.readConfig()

	tickerTask = asyncio.Task(updateTicker())
	socketTask = asyncio.Task(startSocket())
	loop = asyncio.get_event_loop()

	try:
		loop.run_forever()
	except:
		pass

if __name__ == "__main__":
	main()