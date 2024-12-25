import asyncio
import requests
from telegram import Bot

# Bot token and chat ID informations
BOT_TOKEN = "7908853160:AAH9UXA7xw4bjbCW03usgmMjdmyr4bdh3L4"
CHAT_ID = "1277582834"

# A function to take the crypto price
def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

# For sending telegram message
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)
    print("Mesaj gönderildi!")

# Checking bitcoin or any crypto and sending messages
async def monitor_bitcoin_price():
    bitcoin_price = get_crypto_price("bitcoin")
    eth_price = get_crypto_price("ethereum")
    print(f"Bitcoin Fiyatı: ${bitcoin_price}")
    print(f"Ethereum Fiyatı: ${eth_price}")
    if bitcoin_price > 100000:
        await send_telegram_message(f"ALERT! BITCOIN HAS REACHED THE {bitcoin_price}")
    elif eth_price > 1:
        await send_telegram_message(f"ALER! ETHEREUM HAS REACHED THE {eth_price}")
    else:
        await send_telegram_message(f"UPDATED BITCOIN PRICE IS: {bitcoin_price}")
        await send_telegram_message(f"UPDATED ETHEREUM PRICE IS: {eth_price}")

# Loop for constant check
async def main():
    while True:
        await monitor_bitcoin_price()
        await asyncio.sleep(10)  # 60 saniyede bir kontrol

# Anti-senc running
if __name__ == "__main__":
    asyncio.run(main())
