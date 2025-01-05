import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    '''Получает исторические данные об акциях для указанного тикера и временного периода'''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    '''Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия'''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''Вычисляет и выводит среднюю цену закрытия акций за заданный период'''
    average_price = data['Close'].mean()
    print(f"Средняя цена: {average_price:.2f}")
