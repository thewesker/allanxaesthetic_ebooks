'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'JDXcXxwkIXAAOyCCnVJmxMMFA'
MY_CONSUMER_SECRET = 'GBJ17042pZr6osTxbktxBMsE0HcZgmcfkd8dCmD7P5jjdcctMC'
MY_ACCESS_TOKEN_KEY = '2785387999-S1IVuNnJp26jglQ3f3q6e9QgT0Bp9pgwy2prXhD'
MY_ACCESS_TOKEN_SECRET = '2MfmbfATZloTzMNMPSpwkX7Ri4jDuPsd5t1OVIUGiociB'

SOURCE_ACCOUNTS = ["AwfulJack", "mongo_ebooks", "oatgan", "manflurry", "QueenBlappidy", "SlapNutsSA", "GoogTheGoog", "NielJacoby", "KarmineSA"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "BlappidyBot" #The name of the account you're tweeting to.
