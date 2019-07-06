import os
import praw
import access_api
import requests
from tqdm import tqdm


ACCESS_TOKEN, ACCESS_TOKEN_SECRET = access_api.get_reddit_api_keys()


def download_posts(subreddit_):
    reddit = praw.Reddit(client_id=ACCESS_TOKEN, client_secret=ACCESS_TOKEN_SECRET, user_agent='DankMemeBot',
                         username=access_api.USERNAME, password=access_api.PASSWORD)
    subreddit = reddit.subreddit(subreddit_)
    hot = [i.url for i in list(subreddit.hot(limit=10)) if '.jpg' in i.url or '.png' in i.url]

    if not os.path.exists('./imgs'):
        os.makedirs('./imgs')

    count = 0
    for url in tqdm(hot, total=len(hot)):
        file_name = './imgs/meme' + str(count).zfill(2)

        with open(file_name, 'wb') as f:
            response = requests.get(url)
            f.write(response.content)
        count += 1
