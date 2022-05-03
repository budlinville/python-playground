import websocket, json

interval = '1m'
cc = 'btcusdt'
candle_stick = f'kline_{interval}'
stream = f'{cc}@{candle_stick}'
socket = f'wss://stream.binance.com:9443/ws/{stream}'
print(f'socket: {socket}')

closes, highs, lows = [], [], []

def on_message(ws, msg):
    json_msg = json.loads(msg)
    candle = json_msg['k']
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    vol = candle['v']
    
    if is_candle_closed:
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        
        print(closes)
        print(highs)
        print(lows)


def on_close(ws):
    print('Connection Closed')
    
ws = websocket.WebSocketApp(socket, on_message=on_message, on_close = on_close)
ws.run_forever()
