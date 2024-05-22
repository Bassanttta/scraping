from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import schedule


def istricker(word):
    return word[0] == '$' and len(word) <= 4


def scrape_twitter(accounts, interval):
    driver = webdriver.Chrome(service=Service('./chromedriver.exe'))
    mentions = {}  # Dictionary to store mentions for each ticker
    for account in accounts:
        url = f'https://x.com/{account}'
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tweets = soup.find_all('div', {'data-testid': 'tweet'})
        for tweet in tweets:
            for word in tweet.text():
                if istricker(word):
    #print (len(mentions))
    for ticker_symbol, count in mentions.items():
        print(f"The stock ticker '{ticker_symbol}' was mentioned '{count}' times "
              f"in the last '{interval}' minutes.")


def main(accounts, interval):
    schedule.every(interval).minutes.do(scrape_twitter, accounts, interval)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    twitter_accounts = ["RoyLMattox", "Barchart", "CordovaTrades ", "AdamMancini4 ",
                        "TriggerTrades", "yuriymatso", "allstarcharts", "ChartingProdigy",
                        "warrior_0719", "Mr_Derivatives "]
    time_interval = 15  # in minutes
    main(twitter_accounts, time_interval)
