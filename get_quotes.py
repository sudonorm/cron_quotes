import pandas as pd
import requests
import numpy as np
import json
import time
import os


user = os.environ['USERPROFILE']
filePath = os.path.join(os.path.join(user, "Documents"), "daily_quotes.xlsx")
tagIds = []

daily_quotes = pd.read_excel(filePath)

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