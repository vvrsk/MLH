import pandas as pd
import urllib3 as url
import facebook as fb
import json

#Implement Federated Login

#Get the list of pages liked by the user
def getFBResults(token):
	#Connection to graphAPI
	graph = fb.GraphAPI(access_token=token, version = 2.7)
	results = graph.request('me/likes?fields=name,affiliation,category&limit=100')
	return results

#Finding the value of the counts of the user items	
def getPreferredList(results):
	pref_list = []
	tempVal = results.category.value_counts()
	#Manually Setting this for demonstration
	num_pref = 3
	for i in range(0,num_pref):
		pref_list.append(tempVal.index[i])
	return pref_list
	
#Gets Sector Name a corresponding category 	
def getSector(fileName):
	df = pd.DataFrame()
	df = pd.read_csv(fileName,encoding = "ISO-8859-1")
	#We will not consider rows with 'Miscellenous' sector and the affiliation column for this demonstration
	newVals = df.loc[df['Sector'] != 'Miscellaneous']
	newVals = newVals.drop('affiliation',axis=1)
	newVals = newVals[newVals['category'].isin(pref_list)]
	return newVals['Sector']

#Rerturning the JSON File of all data of interest/Output	
def getOutputJSON():
	o = data_ticker[data_ticker['Sector'].isin(p['Sector'])]
	z = (o.groupby(['Sector','Industry'], as_index=False)
       .apply(lambda x: dict(zip(x.Symbol,x.Name)))
       .reset_index()
       .rename(columns={0:'compData'})
       .to_json(orient='records'))
	return z
	
#Write Outputs
def writeOutput(location,fileName):
	cols = ['Sector','Industry']
	vals =o.drop(cols,axis=1)
	vals.to_json(location+'/'+fileName,orient ='records')
	vals.to_csv(location+'/'+fileName,orient ='records')
