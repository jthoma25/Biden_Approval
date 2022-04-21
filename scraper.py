#import numpy as np
#import json
import sys
from sys import maxsize as maxint
import time
from urllib.error import URLError
from http.client import BadStatusLine
from functools import partial

#These two lines fix an issue that I was having with my SSL certificate being verified.
#This is the link to where I found this solution: https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#====================================================================================
#For scraping tweets, we may be able to use the below function and save all of the data to mongoDB
#We just need to figure out how to get tweets from certain points in time



CONSUMER_KEY = 'PMTyrfuGsJiOT3oKIJwfgUHtK'
CONSUMER_SECRET = '473LvEBd5t8v0vTVlLeKq8t4pGGhtLBAJOICDrp5J6mqJulItE'
OAUTH_TOKEN = '952931332266561536-xTABTqG6Z6UGqWsQ22uTrxE8Rzg3WpX'
OAUTH_TOKEN_SECRET = 'xGndkbjVPIPxxFgncJvcvsUnAWX7ze3GMCMxTwCkLIahH'