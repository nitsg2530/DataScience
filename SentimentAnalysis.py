import pandas as pd
import matplotlib.pyplot as plt
import tweepy as tw
from textblob import TextBlob

#Register your app over https://developer.twitter.com/ to obtain below keys from Twitter
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Below parameters can be inputs 
search_handle = "#Trump"
numer_of_tweets= 100

# Create a custom search term and define the number of tweets
search_term = search_handle +" -filter:retweets"

tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since='2018-01-01').items(numer_of_tweets)


# Create textblob objects of the tweets
sentiment_objects = [TextBlob(tweet.text) for tweet in tweets]

# Create list of polarity valuesx and tweet text
polarity_values = [[tweet.sentiment.polarity, tweet.sentiment.subjectivity, str(tweet)] for tweet in sentiment_objects]

# Create dataframe containing the polarity value and tweet text
polarity_df = pd.DataFrame(polarity_values, columns=["polarity","subjectivity", "tweet"])

polarity_df.head()

fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram of the polarity values
polarity_df["polarity"].hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="orange",alpha=0.35)
polarity_df["subjectivity"].hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="green",alpha=0.35)
plt.title("Sentiments from Tweets on "+ search_handle)
plt.ylabel('Parameter count')
plt.xlabel('Sentiments +ve or -ve')

plt.show()


