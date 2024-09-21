# Binance WebSocket Client

Binance WebSocket Client for Real-Time Trade Data by Taylor Christian Newsome

This Python script establishes a WebSocket connection to Binance's futures market (wss://fstream.binance.com/ws) to receive real-time trade data for specific cryptocurrency pairs, such as BTC/USDT. The script handles WebSocket events including:

- **Ping-Pong Handling**: Automatically responds to server pings to keep the connection alive.
- **Message Processing**: Receives and logs real-time messages, such as trade data or order book updates, in JSON format.
- **Automatic Reconnection**: Attempts to reconnect after unexpected connection closures or errors.
- **Logging**: Detailed logging of WebSocket events (connections, messages, errors) for easier debugging and monitoring.

## Key Features:
- Subscribes to trade streams by default, but can be extended to other streams.
- Implements reconnection logic with a 5-second retry delay.
- Error handling and automatic ping-pong responses to maintain a stable WebSocket connection.

## Usage:
Simply run the script to start receiving and logging real-time trade data from Binance. The `on_message` function can be modified to process trade data or other event types according to your needs.

[Proof of Concept](https://www.youtube.com/watch?v=CXruFsa1SMQ)

Watch the proof of concept video on YouTube.
