from pandas import DataFrame, read_csv
import pandas as pd 
import operator

#we return a dictionary holding information about each account that 
#mentined at least once the NGO for fighting disinformation.
#The dictionary holds the username of the account, an associated X point, that represents the
#number of tweets about the NGO that account generated, and Y point that denotes
#the number of retweets that the accounts content about the NGO received. 
#You can use the dictionary to then easily plot the points.


def readTextcovid():
	
	#file = r'covidmx.csv'
	file = r'esp_covid19.csv'
	df = pd.read_csv(file)
	
	
	usernamesDict={}
	for i in df.index:
		
		username=df['usernameTweet'][i]
		numRetweets=df['nbr_retweet'][i]
		
		usernamesDict.setdefault(username,{})
		usernamesDict[username].setdefault("x",0)
		usernamesDict[username].setdefault("y",0)
		usernamesDict[username]["x"]+=1
		usernamesDict[username]["y"]+=numRetweets
	return usernamesDict

	
readTextcovid()