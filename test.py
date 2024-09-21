import websocket
import logging
import time

# Logger setup
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(handler)

# Binance WebSocket URL
BINANCE_WS_URL = 'wss://fstream.binance.com:443/ws'

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
    log.info(f"Received message: {message}")

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
        ws.run_forever()  # Reconnect automatically
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
        on_close=on_close
    )
    try:
        ws.run_forever()  # Keep the connection open
    except Exception as e:
        log.error(f"Error while running WebSocket: {e}")
        reconnect(ws)

if __name__ == "__main__":
    connect()
