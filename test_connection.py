from bot.client import get_client

client = get_client()

try:
    account = client.futures_account()

    print("AUTH SUCCESS")
    print("Can Trade:", account.get("canTrade"))

except Exception as e:
    print("AUTH FAILED")
    print(e)