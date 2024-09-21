import websocket
import json
import logging
import time

# Logger setup
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(handler)

# Binance WebSocket URL
BINANCE_WS_URL = 'wss://fstream.binance.com/ws'

def on_ping(ws, message):
    try:
        ws.pong()  # Automatically send pong when receiving ping
        log.info('Received ping from server, sent pong back')
    except websocket.WebSocketConnectionClosedException:
        log.error('WebSocket connection closed unexpectedly.')
        reconnect(ws)
    except Exception as e:
        log.error(f'Error during ping handling: {e}')

def on_message(ws, message):
    try:
        data = json.loads(message)
        log.info(f"Received message: {data}")
        # You can process the message further, e.g., print trade data, order book updates, etc.
    except Exception as e:
        log.error(f"Error processing message: {e}")

def on_open(ws):
    log.info("WebSocket connected, subscribing to stream...")
    # Example subscription to BTC/USDT trades stream
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params": [
            "btcusdt@trade"  # You can add more streams here
        ],
        "id": 1
    }
    ws.send(json.dumps(subscribe_message))  # Send the subscription message
    log.info("Subscribed to BTC/USDT trades")

def on_close(ws, close_status_code, close_msg):
    log.warning(f"WebSocket closed with status: {close_status_code}, message: {close_msg}")
    reconnect(ws)

def on_error(ws, error):
    log.error(f"WebSocket error: {error}")
    reconnect(ws)

def reconnect(ws):
    log.info('Attempting to reconnect...')
    time.sleep(5)  # Wait before reconnecting
    try:
        connect()  # Reconnect by calling the connect function again
        log.info('Reconnected successfully.')
    except Exception as e:
        log.error(f"Reconnection failed: {e}")

def connect():
    websocket.enableTrace(True)  # Optional, for debugging purposes
    ws = websocket.WebSocketApp(
        BINANCE_WS_URL,
        on_ping=on_ping,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open  # Handle subscription when WebSocket opens
    )
    try:
        ws.run_forever()  # Keep the connection open
    except Exception as e:
        log.error(f"Error while running WebSocket: {e}")
        reconnect(ws)

if __name__ == "__main__":
    connect()
