import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите порог изменения цен, при преодолении которого появится уведомление (например, '0.05' для 5%): "))

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data, rsi, macd
    rsi = input("Нужен ли график RSI(y/n)?")
    rsi = True if rsi=='y' else False

    macd = input("Нужен ли график MACD(y/n)?")
    macd = True if macd == 'y' else False
    dplt.create_and_save_plot(data=stock_data, ticker=ticker, period=period, rsi=rsi, macd=macd)

    # Print the average price
    dd.calculate_and_display_average_price(stock_data)

    # Print if the price is above the threshold
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Make CSV
    make_csv = input("Хотите выгрузить результат в csv файл(y/n)? ")
    if make_csv == 'y':
        csv_name = input("Введите название файла: ")
        dd.export_data_to_csv(stock_data, csv_name)

if __name__ == "__main__":
    main()
