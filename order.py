from binance.client import Client
import time

api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

# correct client (no manual URL change)
client = Client(api_key, api_secret)

# correct testnet futures
client.FUTURES_URL = "https://testnet.binancefuture.com"

print("Starting bot...")

try:
    print("Placing order...")

    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print("Order placed successfully")
    print(order)

except Exception as e:
    print("Error occurred")
    print(e)