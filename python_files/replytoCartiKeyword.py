# reply to people who have the word carti in their tweet
from cartiMain import myStream, myStreamListener, api



def whoTweetingCarti():
    print('looking for people who have said carti!')
    myStream.filter(track=['carti'], is_async=True)

def turnOnReplyKeywordCarti(status):
    while status == True:
        whoTweetingCarti()
