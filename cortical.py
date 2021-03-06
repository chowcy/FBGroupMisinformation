import retinasdk
import json
import config

def get_keywords(text):
  fullClient = retinasdk.FullClient(config.cortical_api_key, apiServer="http://api.cortical.io/rest", retinaName="en_associative")
  keywords = fullClient.getKeywordsForText(text)
  return (keywords)

sample = "Iraq War Vet Who Lost His Leg in Battle Shuts Down David Hogg With Brutal Message"
s1 = "Frank Stallone apologizes 'to David Hogg especially' for profane Parkland tweetAfter attacking David Hogg, a gun-control activist who survived the Parkland, Fla., school shooting, Frank STallone is apologizing"


# print (get_keywords(s1))
