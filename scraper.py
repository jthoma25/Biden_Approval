import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import twitter
import networkx as nx
import matplotlib.pyplot as plt



#authentication function that deems I am me through my keys and create an
#instance of the twitter API for future use
def oauth_login():
    CONSUMER_KEY = 'pg21VyTbJnJL3qfu8AW4LRMMq'
    CONSUMER_SECRET = 'rrYiaGfUoxN70tM4e5I8SwH31uJUmYP5mxBjzEv0Zowdh'
    OAUTH_TOKEN = '952931332266561536-Y1D9ggfrZTP72HIMGkEaz1Uxf5OuP55'
    OAUTH_TOKEN_SECRET = 'rrYiaGfUoxN70tM4e5I8SwH31uJUmYP5mxBjzEv0Zowdh'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

twitter_api = oauth_login()

print(twitter_api)

#taken from cookbook
def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw): 
    
    # A nested helper function that handles common HTTPErrors. Return an updated
    # value for wait_period if the problem is a 500 level error. Block until the
    # rate limit is reset if it's a rate limiting issue (429 error). Returns None
    # for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
    
        if wait_period > 3600: # Seconds
            print('Too many retries. Quitting.', file=sys.stderr)
            raise e
    
        # See https://developer.twitter.com/en/docs/basics/response-codes
        # for common codes
    
        if e.e.code == 401:
            print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
            return None
        elif e.e.code == 404:
            print('Encountered 404 Error (Not Found)', file=sys.stderr)
            return None
        elif e.e.code == 429: 
            print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
            if sleep_when_rate_limited:
                print("Retrying in 15 minutes...ZzZ...", file=sys.stderr)
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print('...ZzZ...Awake now and trying again.', file=sys.stderr)
                return 2
            else:
                raise e # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered {0} Error. Retrying in {1} seconds'                  .format(e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e

    # End of nested helper function
    
    wait_period = 2 
    error_count = 0 

    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0 
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("URLError encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise
        except BadStatusLine as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("BadStatusLine encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise


#list of keywords for search
q = 'Joe Biden, Biden, President Biden, State of the Union, State of the Union Address, NATO Summit'

#Nov 10th
#=============================================================================================================================================
responseNov10Before = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-11-10T00:00:00'), end_time = ('2022-11-10T23:59:59')))
responseNov10After = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-11-11T00:00:00'), end_time = ('2022-11-11T23:59:59')))
#send data to file
Nov10 = open('CIS400_Nov10', 'w')
Nov10.write('Before', 'w')
Nov10.writelines(responseNov10Before)
Nov10.write('\n\n')
Nov10.write('After', 'w')
Nov10.writelines(responseNov10After)
Nov10.write('\n\n')
Nov10.close()


#=============================================================================================================================================
#Feb 24th
#=============================================================================================================================================
responseFeb24Before = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-02-24T00:00:00'), end_time = ('2022-02-24T01:43:00')))
responseFeb24After = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-02-24T02:05:00'), end_time = ('2022-02-24T23:59:59')))
#send data to file
Feb24 = open('CIS400_Feb24', 'w')
Feb24.write('Before', 'w')
Feb24.writelines(responseFeb24Before)
Feb24.write('\n\n')
Feb24.write('After', 'w')
Feb24.writelines(responseFeb24After)
Feb24.write('\n\n')
Feb24.close()


#=============================================================================================================================================
#Mar 1st
#=============================================================================================================================================
responseMar01Before = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-03-01T00:00:00'), end_time = ('2022-03-01T21:00:00')))
responseMar01After = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-03-01T22:33:40'), end_time = ('2022-03-01T23:59:59')))
#send data to files according to time stamps.
Mar01 = open('CIS400_Mar01', 'w')
Mar01.write('Before', 'w')
Mar01.writelines(responseMar01Before)
Mar01.write('\n\n')
Mar01.write('After', 'w')
Mar01.writelines(responseMar01After)
Mar01.write('\n\n')
Mar01.close()


#=============================================================================================================================================
#Mar 26th
#=============================================================================================================================================
responseMar24Before = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-03-24T00:00:00'), end_time = ('2022-03-24T11:59:59')))
responseMar24After = make_twitter_request(twitter_api.search.tweets(q = q, count = 150, start_time = ('2022-03-25T:00:00:00'), end_time = ('2022-03-25T11:59:59')))
#send data to files according to time stamps.
Mar24 = open('CIS400_Mar26', 'w')
Mar24.write('Before', 'w')
Mar24.writelines(responseMar24Before)
Mar24.write('\n\n')
Mar24.write('After', 'w')
Mar24.writelines(responseMar24After)
Mar24.write('\n\n')
Mar24.close()


#=============================================================================================================================================

