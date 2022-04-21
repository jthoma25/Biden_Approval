# CIS 400
# Sentiment analysis
# 
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


def clean_tweet (tweet):
    # remove the retweet symbol "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove any URLs present in the tweets
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    # remove the # and @ characters
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'@', '', tweet)

    # remove any digits 
    tweet = re.sub("\d+", " ", tweet)

    #remove punctuation marks
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for p in tweet:
        if p in punc:
            tweet = tweet.replace(p, "")

    # remove emojis from tweet
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF" 
        u"\U00002500-\U00002BEF"  
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f" 
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', tweet)


def process_tweet(tweet):
    # remove stop wrods such as the, in, a, of etc. from tweet
    simplified_tweet = stopwords.words('english')

    # tokenize tweets
    tweet_tokens = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True).tokenize(tweet)

    # use the stem of the word 
    processed_tweet = ''
    for word in tweet_tokens:
        if word not in simplified_tweet:
            stem = WordNetLemmatizer().lemmatize(word)
            processed_tweet += ' ' + stem

    return processed_tweet

def analyis(tweet):
    # get the sentiment scores using VADER
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(tweet)

    # retrieve the compound score
    score = scores.get('compound')

    # categorize based on the compound score
    if score >= 0.05:
        classification = 'positive'
    elif score <= -0.05:
        classification = 'negative'
    else:
        classification = 'neutral'

    return classification



def main():
#April 13th
#=============================================================================================================================
    file_negatives= open("Apr_13_negative_tweets.txt","w+")
    file_positives= open("Apr_13_positive_tweets.txt","w+")
    file_neutrals= open("Apr_13_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr13.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 13 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 14th
#=============================================================================================================================

    file_negatives= open("Apr_14_negative_tweets.txt","w+")
    file_positives= open("Apr_14_positive_tweets.txt","w+")
    file_neutrals= open("Apr_14_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr14.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 14 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 15th
#=============================================================================================================================

    file_negatives= open("Apr_15_negative_tweets.txt","w+")
    file_positives= open("Apr_15_positive_tweets.txt","w+")
    file_neutrals= open("Apr_15_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr15.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 15 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 16th
#=============================================================================================================================

    file_negatives= open("Apr_16_negative_tweets.txt","w+")
    file_positives= open("Apr_16_positive_tweets.txt","w+")
    file_neutrals= open("Apr_16_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr16.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 16 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 17th
#=============================================================================================================================

    file_negatives= open("Apr_17_negative_tweets.txt","w+")
    file_positives= open("Apr_17_positive_tweets.txt","w+")
    file_neutrals= open("Apr_17_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr17.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 17 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 18th
#=============================================================================================================================

    file_negatives= open("Apr_18_negative_tweets.txt","w+")
    file_positives= open("Apr_18_positive_tweets.txt","w+")
    file_neutrals= open("Apr_18_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr18.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 18 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 19th
#=============================================================================================================================

    file_negatives= open("Apr_19_negative_tweets.txt","w+")
    file_positives= open("Apr_19_positive_tweets.txt","w+")
    file_neutrals= open("Apr_19_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr19.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 19 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()

#April 20th
#=============================================================================================================================

    file_negatives= open("Apr_20_negative_tweets.txt","w+")
    file_positives= open("Apr_20_positive_tweets.txt","w+")
    file_neutrals= open("Apr_20_neutral_tweets.txt","w+")

    positives = 0
    negatives = 0
    neutrals = 0
    
    tweets_file=open("CIS400_Apr20.txt", "r")

    for tweet in tweets_file:
        if tweet != "\n":
            rating = analyis(process_tweet(clean_tweet(tweet)))
        
            if rating == 'negative':
                file_negatives.write(tweet + "\n\n")
                negatives += 1
            elif rating == 'neutral':
                file_neutrals.write(tweet + "\n\n")
                neutrals += 1
            elif rating == 'positive':
                file_positives.write(tweet + "\n\n")
                positives += 1

    print("\nApril 20 \n")
    print("Number of negative tweets: " + str(negatives))
    print("Number of positive tweets: " + str(positives))
    print("Number of neutral tweets: " + str(neutrals))
    print("----------------------------------------------")
    file_negatives.close()
    file_positives.close()
    file_neutrals.close()
    tweets_file.close()



if __name__ == "__main__":
    main()