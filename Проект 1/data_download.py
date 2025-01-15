import yfinance as yf
import csv


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


def notify_if_strong_fluctuations(data, threshold):
    '''Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период'''
    price_changes = data['Close'].pct_change()
    max_change = price_changes.abs().max()

    if max_change > threshold:
        print(f"Изменение цены выше порога: {max_change}!")
    else:
        print(f"Изменения цены выше порога не замечено.")

def export_data_to_csv(data, filename):
    '''Позволяет сохранять загруженные данные об акциях в CSV файл'''
    data.to_csv(filename+'.csv', index=False)
    print("CSV файл сохранён")
