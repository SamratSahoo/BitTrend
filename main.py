from cryptocmd import CmcScraper
import matplotlib.pyplot as plt


def main():
    figure, coin = ask_and_draw()
    save_figure(figure, coin)


def ask_and_draw():
    coin = input("What cryptocurrency would you like to see trends for?\n").strip()
    scraper = CmcScraper(coin)
    df = scraper.get_dataframe()
    close_data = df['Close'][::-1]
    time_data = range(0, len(close_data))

    plt.plot(time_data, close_data)
    plt.xlabel("Days Since " + str(list(df['Date'])[-1]))
    plt.ylabel("Price of " + coin + " (USD)")
    figure = plt.gcf()
    plt.show()
    return figure, coin


def save_figure(figure, coin):
    save_ans = input("Would you like to save this trend (y/n)?\n")
    if save_ans == "y":
        figure.savefig(coin.lower() + "_all_time.png")
    else:
        print("Aborting Program; Not Saving Trend")


if __name__ == '__main__':
    main()
