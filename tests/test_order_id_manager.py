from app.execution.order_id_manager import OrderIDManager

manager = OrderIDManager()

for _ in range(5):

    print(manager.generate())