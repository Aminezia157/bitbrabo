from binance.client import Client
import time

# Suas chaves da API Binance
API_KEY = 'SUA_API_KEY_AQUI'
SECRET_KEY = 'SEU_SECRET_KEY_AQUI'

# Inicializar o cliente da Binance
client = Client(API_KEY, SECRET_KEY)

def get_bitcoin_price():
    try:
        # Buscar o preço atual do par BTC/USDT
        ticker = client.get_symbol_ticker(symbol="BTCUSDT")
        return ticker['price']
    except Exception as e:
        print(f"Erro ao buscar o preço: {e}")
        return None

# Verificar o preço a cada 60 segundos
while True:
    price = get_bitcoin_price()
    if price:
        print(f"O preço do Bitcoin (BTC/USDT) é: ${price}")
    else:
        print("Não foi possível obter o preço do Bitcoin.")
    
    # Esperar 60 segundos antes de verificar novamente
    time.sleep(60)