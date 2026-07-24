from app.market.websocket_manager import WebSocketManager

ws = WebSocketManager()

ws.print()

print()

ws.connect(

    "wss://stream.binance.com:9443/ws/btcusdt@trade"

)

ws.print()

print()

print(ws.status())

print()

ws.disconnect()

ws.print()