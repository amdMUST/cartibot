
import tweepy as tp # to use the twitter API
import time # to specify how much time in between tweets
import os # to move to the cartiPics folder

# creds to login to api
consumerKey = 'NdFFEbjRY3P1V0mgNz3rAzTHN'
consumerSec = 'hHwErqiswcARJeCjSQWG6DP5j1zlPkoblh3UbQTxGTAcq9PA8o'
accessTok = '1174077014275502080-Kpg7KmUFSSyQVfuqm8jbABli5g7aEf'
accessSec = 'nNDhR5kjtZdLLSx8UX70J45YXVkoVa7LB3IhrUe5uFHHl'

# loging in
auth = tp.OAuthHandler(consumerKey,consumerSec)
auth.set_access_token(accessTok,accessSec)
api = tp.API(auth)


# new picture in imgs folder
os.chdir('cartiPics')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(30000000)