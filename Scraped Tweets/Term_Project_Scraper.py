import twitter

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#authentication function that deems I am me through my keys and creates an
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

#April 13th
#=============================================================================================================================
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
Apr13 = open('CIS400_Apr13.txt', 'w')

for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-14', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            #This filters out the Retweets and tweets that were broken up into more than one tweet using '…'.
            Apr13.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr13.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr13.close()


#April 14th
#=============================================================================================================================
Apr14 = open('CIS400_Apr14.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-15', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr14.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr14.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr14.close()


#April 15th
#=============================================================================================================================
Apr15 = open('CIS400_Apr15.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-16', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr15.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr15.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr15.close()


#April 16th
#=============================================================================================================================
Apr16 = open('CIS400_Apr16.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-17', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr16.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr16.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr16.close()


#April 17th
#=============================================================================================================================
Apr17 = open('CIS400_Apr17.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-18', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr17.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr17.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr17.close()


#April 18th
#=============================================================================================================================
Apr18 = open('CIS400_Apr18.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-19', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr18.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr18.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr18.close()


#April 19th
#=============================================================================================================================
Apr19 = open('CIS400_Apr19.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-20', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr19.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr19.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr19.close()


#April 20th
#=============================================================================================================================
Apr20 = open('CIS400_Apr20.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-21', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr20.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr20.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr20.close()


#April 21st
#=============================================================================================================================
Apr21 = open('CIS400_Apr21.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-22', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr21.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr21.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr21.close()


#April 22nd
#=============================================================================================================================
Apr22 = open('CIS400_Apr22.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-23', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr22.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr22.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr22.close()


#April 23rd
#=============================================================================================================================
Apr23 = open('CIS400_Apr23.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-24', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr23.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr23.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr23.close()


#April 24th
#=============================================================================================================================
Apr24 = open('CIS400_Apr24.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-25', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr24.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr24.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr24.close()


#April 25th
#=============================================================================================================================
Apr25 = open('CIS400_Apr25.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-26', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr25.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr25.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr25.close()


#April 26th
#=============================================================================================================================
Apr26 = open('CIS400_Apr26.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-27', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr26.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr26.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr26.close()


#April 27th
#=============================================================================================================================
Apr27 = open('CIS400_Apr27.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-28', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr27.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr27.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr27.close()


#April 28th
#=============================================================================================================================
Apr28 = open('CIS400_Apr28.txt', 'w')
#Creates a file that stores the tweets. Overwrites the file if the file already exists, and creates one if it does not.
for i in q:
    #A loop that goes through the keywords stored in q above, and uses those to obtain any tweets that contain the keywords in q.
    #Obtains only 100 tweets as is limited by the api, uses 'until' to get tweets only up to that date.
    #Uses a mixed 'result_type' which gets a combination of the most popular tweets, along with the most recent tweets to get 
    #a variety of tweets and opinions.
    #Uses the 'lang' keyword with 'en' to only obtain tweets that are in English
    response = twitter_api.search.tweets(q = i, count = 100, until = '2022-04-29', result_type = 'mixed', lang = 'en')
    for j in range(len(response['statuses'])):
        #After the tweets are obtained, we go through each tweet and obtain only the text for the tweet.
        if 'RT' not in response['statuses'][j]['text'] and '…' not in response['statuses'][j]['text']:
            Apr28.write(response['statuses'][j]['text'].replace('\n', ' '))
            #Tweet is then written to the file and any newline characters are removed.
            #We then add three newlines to break up each tweet.
            Apr28.write('\n\n\n')
#The file is closed once the tweets have been obtained and correctly written to the file.
Apr28.close()

