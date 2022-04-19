import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import twitter
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta, date

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#authentication function that deems I am me through my keys and create an
#instance of the twitter API for future use
def oauth_login():
    CONSUMER_KEY = 'sLefLt7nNMZ9s0zMPwBH4hvcS'
    CONSUMER_SECRET = 'Q2em8B4mKltPRZ6xisCJuE6Nh0EiRtTKp6oqB1F0fhIcWGsnEC'
    OAUTH_TOKEN = '2201007353-YK2FLO7szMp8pY7jGKnpoDORxgf3LIB82GYuASj'
    OAUTH_TOKEN_SECRET = 'WtwYfBDcyqgSUeJq6CS2gYXm3NiVc262NYYDD1naMeZO2'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

twitter_api = oauth_login()






#list of keywords for search
q = ['Biden', 'President Biden', 'Joe Biden', '#Biden', '#PresidentBiden', '#JoeBiden', 'POTUS', '#POTUS']


'''
Each of the below dates work the same way. They each open their respective date's file and loops through 100 tweets from that day
using the parameters q which is the keyword, count which is capped at 100 tweets by the api, until which helps to get tweets from a certain date,
result_type which shows a mix of popular and the most recent tweets, and finally lang which is set to 'en' so that we only get english results.

We begin with a for loop that loops through the keywords above and passes them into q as i. We then take the tweets that were gathered
from that q keyword and loop through that. We filter out all retweets and all of those that have tweets broken up by '…'. We then break down the output of
the api call until we get to the tweet text, and we write to the given txt files for that date.

'''
#April 11th
#=============================================================================================================================
Apr11 = open('CIS400_Apr11.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-12', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr11.write(response['statuses'][j]['text'])
            Apr11.write('\n\n\n')
Apr11.close()


#April 12th
#=============================================================================================================================
Apr12 = open('CIS400_Apr12.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-13', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr12.write(response['statuses'][j]['text'])
            Apr12.write('\n\n\n')
Apr12.close()


#April 13th
#=============================================================================================================================
Apr13 = open('CIS400_Apr13.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-14', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr13.write(response['statuses'][j]['text'])
            Apr13.write('\n\n\n')
Apr13.close()


#April 14th
#=============================================================================================================================
Apr14 = open('CIS400_Apr14.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-15', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr14.write(response['statuses'][j]['text'])
            Apr14.write('\n\n\n')
Apr14.close()


#April 15th
#=============================================================================================================================
Apr15 = open('CIS400_Apr15.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-16', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr15.write(response['statuses'][j]['text'])
            Apr15.write('\n\n\n')
Apr15.close()


#April 16th
#=============================================================================================================================
Apr16 = open('CIS400_Apr16.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-17', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr16.write(response['statuses'][j]['text'])
            Apr16.write('\n\n\n')
Apr16.close()


#April 17th
#=============================================================================================================================
Apr17 = open('CIS400_Apr17.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-18', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr17.write(response['statuses'][j]['text'])
            Apr17.write('\n\n\n')
Apr17.close()


#April 18th
#=============================================================================================================================
Apr18 = open('CIS400_Apr18.txt', 'w')

for i in q:
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-19', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr18.write(response['statuses'][j]['text'])
            Apr18.write('\n\n\n')
Apr18.close()


#=============================================================================================================================


