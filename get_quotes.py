import requests
import pandas as pd
import numpy as np
import json
import time
import os
import argparse

def get_quote(userName = ""):
    '''
        This function, used as an input in a Jenkins cron job, runs daily in order to get a quote from an api and save to a file.
        Note that the current userPath assumes the OS environment is Windows.
    '''

    userPath = os.path.join("C:\\Users\\" , userName)
    filePath = os.path.join(os.path.join(userPath, "Documents"), "daily_quotes.xlsx")
    print(filePath)
    tagIds = []

    try:
        daily_quotes = pd.read_excel(filePath)
    except:
        daily_quotes = pd.DataFrame(columns=["id", "day", "author", "quote", "tagId"])

    if len(daily_quotes) == 0:
        fid = 1
    else:
        fid = len(daily_quotes) + 1
        tagIds = list(daily_quotes["tagId"])

    url = "https://type.fit/api/quotes"
    quote = requests.get(url)
    print("Getting quote...")

    if quote.status_code == 200:
        quotes = json.loads(quote.content)
        quotes_df = pd.DataFrame(quotes)

        if len(tagIds) == 0:
            randomQuote = quotes_df.sample(1).reset_index()
            tagId = list(randomQuote["index"])[0]
            qte = list(randomQuote["text"])[0]
            auth = list(randomQuote["author"])[0]
        else:
            randomQuote = quotes_df.sample(1).reset_index()
            tagId = list(randomQuote["index"])[0]

            while tagId in tagIds:
                randomQuote = quotes_df.sample(1).reset_index()
                tagId = list(randomQuote["index"])[0]
    
            qte = list(randomQuote["text"])[0]
            auth = list(randomQuote["author"])[0]

        daily_quotes = daily_quotes.append({"id": fid, "day": time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()), "author": auth, "quote": qte, "tagId": tagId}, ignore_index=True)
        print("Saving file...")
        daily_quotes.to_excel(filePath, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", action='store')
    args = parser.parse_args()
    userName = args.user
    print("user is: " + userName)
    get_quote(userName)