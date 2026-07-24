from app.market.websocket_manager import WebSocketManager
from app.market.multi_exchange_feed_manager import MultiExchangeFeedManager

binance = WebSocketManager()
bybit = WebSocketManager()
mt5 = WebSocketManager()

binance.endpoint = "wss://stream.binance.com/ws/btcusdt@trade"
bybit.endpoint = "wss://stream.bybit.com/v5/public/linear"
mt5.endpoint = "mt5://terminal"

manager = MultiExchangeFeedManager()

manager.register("Binance", binance)
manager.register("Bybit", bybit)
manager.register("MT5", mt5)

manager.connect_all()

manager.print()

print()
print(manager.status())

manager.disconnect_all()

print()
manager.print()