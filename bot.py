import asyncio
from twikit import Client
from datetime import datetime, date, time, timedelta
import time
import os

USERNAME = os.getenv("USERNAME") 
EMAIL =os.getenv("EMAIL") 
PASSWORD = os.getenv("PASSWORD")

client = Client(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
)

keywords = ['bitshift', 'game', "chest", "lever", "program", "tool", "ai", "js", "java", "script", "dev", "dungeon", "crawler", "lac", "ui", "inventor", "look", "release", "engine", "daryl"]

def wilm(dt: datetime) -> bool:
    now = datetime.now().timestamp()
    if now - dt.timestamp() <= 60:
        return True
    else:
        return False

async def check():

    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    tweets = await client.get_user_tweets('63485337', 'Tweets')
    for tweet in tweets:
        if wilm(tweet.created_at_datetime):
            if any(keyword in tweet.text.lower() for keyword in keywords):
                return tweet.text

