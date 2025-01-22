import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import data_download as dd


def create_and_save_plot(data, ticker, period, filename=None, rsi=True, macd=True):

    fig, axes = plt.subplots(nrows=3 if rsi and macd else (2 if rsi or macd else 1),
                             figsize=(12, 8), sharex=True)

    if not isinstance(axes, np.ndarray):
        axes = [axes]

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        dates = data['Date']


    axes[0].plot(dates, data['Close'].values, label='Close Price')
    axes[0].plot(dates, data['Moving_Average'].values, label='Moving Average')
    axes[0].set_title(f"{ticker} Цена акций с течением времени")
    axes[0].set_ylabel("Цена")
    axes[0].legend()

    if rsi:
        rsi_values = dd.rsi(data)
        if rsi_values is not None:
            axes[1].plot(dates, rsi_values, label='RSI')
            axes[1].axhline(80, color='red', linestyle='--')  # Линия перекупленности
            axes[1].axhline(20, color='green', linestyle='--')  # Линия перепроданности
            axes[1].set_title("RSI")
            axes[1].set_ylabel("Значение RSI")
            axes[1].legend()

    if macd:
        macd_data = dd.macd(data)
        if macd_data is not None:
            axes[2].plot(dates, macd_data['MACD'], label='MACD', color='blue')
            axes[2].plot(dates, macd_data['Signal'], label='Сигнальная линия', color='orange')
            axes[2].bar(dates, macd_data['Histogram'], label='Гистограмма MACD', color='gray')
            axes[2].set_title("MACD")
            axes[2].set_ylabel("Значения MACD")
            axes[2].legend()

    plt.xlabel("Дата")
    plt.tight_layout()
    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")