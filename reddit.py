import praw
from config import reddit_config
import pandas as pd

reddit = praw.Reddit(client_id=reddit_config['client_id'],
                          client_secret = reddit_config['secret'],
                          user_agent = reddit_config['user_agent'],
                          username= reddit_config['username'],
                          password= reddit_config['password'])

def create_topics():
    global topics
    topics = {'title': [],
              'url': [],
              'body': []
              }
    return topics

def get_text(post):
    title = post.title
    url = post.url
    topics['title'].append(post.title)
    topics['url'].append(post.url)
    topics['body'].append(post.selftext)
    text = f'{title}, {url}'
    return text

async def get_body(message):
    topics_data = pd.DataFrame(topics)
    body = topics_data['body']
    text = body[int(message.content)]
    return text

async def get_hot(message, parts):
    posts = reddit.subreddit(parts[1])
    sends = []
    create_topics()
    for post in posts.hot(limit=int(parts[2])):
        text = get_text(post)
        sends.append(text)
    return sends

async def get_top(message, parts):
    posts = reddit.subreddit(parts[1])
    sends = []
    create_topics()
    for post in posts.top(limit=int(parts[2])):
        text = get_text(post)
        sends.append(text)
    return sends

async def get_new(message, parts):
    posts = reddit.subreddit(parts[1])
    sends = []
    create_topics()
    for post in posts.new(limit=int(parts[2])):
        text = get_text(post)
        sends.append(text)
    return sends



