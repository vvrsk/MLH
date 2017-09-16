
# coding: utf-8

# In[1]:

#Modules Import
import pandas as pd
import urllib3 as url
import facebook as fb
import json


# In[2]:

#My token for App
token= 'EAACBZAD5dy10BAJh49XPM8XFNjNwJ0cNCEbg9Sev3P3e8ZAjahzJFuXeXIxDHJIo3WmYYfg8LfMHbOrCpTFZAicqvwGZC6eIKC6kZCo0oamjew0BNeSTeeRRUCVSGB3onFesaW6GbQmuPn9Ea6ZBf5MqL2BZAvi7jAZD'  
# 'aiufniqaefncqiuhfencioaeusKJBNfljabicnlkjshniuwnscslkjjndfi'


# In[3]:

#Connection to graphAPI
graph = fb.GraphAPI(access_token=token, version = 2.7)


# In[ ]:

#test
#ip_query = input('Enter type of items you want to retreive, (event/status/status_id)')
#req_query = input('What kind of event do you want data of?? (poetry/juggling/ etc....)')


# In[ ]:

#Test -2
#results = graph.request('/search?q='+req_query+'&type='+ip_query+'&limit=10000')


# In[141]:

#Request for the page Likes of user. _ Here the user is currently me But it should be replaced with
# USER Id of the user we would like to get.
results2 = graph.request('me/likes?fields=name,affiliation,category&limit=100')


# In[ ]:

#results2['data']
#len(results2['data'])


# In[142]:

http = url.PoolManager()
i=0
count=0
#final_json= []
while 'paging' in results2:
    #while not(not results2['paging']['next']):
        i=i+1
        r = http.request('GET', results2['paging']['next'])
        str_data=r.data
        print(type(str_data))
        my_json = str_data.decode('utf8')
        data = json.loads(my_json)
        s1 = json.dumps(data, indent=4, sort_keys=True)
       
        #final_json.append(s1)
        #print("The Next URL is: "+results2['paging']['next'])
        results2=json.loads(s1)
        with open('C:/Users/vvrsk/Desktop/Test- Json/final_json_%s.txt'%i, 'w') as outfile:
            json.dump(results2, outfile)
        count=i
        #print(results2['data'])
print("Final Count of URL's & Files ",count)


# In[140]:

http = url.PoolManager()
i=0
count=0
#final_json= []
finalDF = pd.DataFrame()
while 'paging' in results2:
    #while not(not results2['paging']['next']):
        i=i+1
        r = http.request('GET', results2['paging']['next'])
        str_data=r.data
        my_json = str_data.decode('utf8')
        data = json.loads(my_json)
        s1 = json.dumps(data, indent=4, sort_keys=True)
        #final_json.append(s1)
        #print("The Next URL is: "+results2['paging']['next'])
        results2=json.loads(s1)
        #print(type(results2))
        finalDF = finalDF.append(pd.DataFrame.from_dict(results2['data']),ignore_index = True)
        #with open('C:/Users/vvrsk/Desktop/Test- Json/final_json_%s.txt'%i, 'w') as outfile:
        #    json.dump(results2, outfile)
        #count=i
        #print(i)
        print(type(str_data))
        #print(finalDF.shape)
        #print(results2['data'])
print("Final Count of URL's & Files ",i)


# In[ ]:

#finalDF.category.unique()


# In[ ]:

#File downloaded for the sector assignment
#finalDF.to_csv('C:/Users/vvrsk/Desktop/Test- Json/hello.csv', sep=',')
#list1 = finalDF.category.unique().tolist()


# In[ ]:

#data_ticker.Industry.str.contains('Newspaper')


# In[6]:

#Finding the value of the counts of the user items
# Cleaning The data required pending step.
a = finalDF.category.value_counts()
pref_list = []
#Number of Preferences to be displayed = 3
num_pref = 3
#Populating the preference list.
for i in range(0,num_pref):
    pref_list.append(a.index[i])
print(pref_list)

#Getting the category of the pref_list
#for item in pref_list:
#    category_tList = item['Sector']


# In[38]:

df = pd.DataFrame()
df = pd.read_csv('C:/Users/vvrsk/Desktop/Test- Json/hello2.csv',encoding = "ISO-8859-1")

newVals = df.loc[df['Sector'] != 'Miscellaneous']
newVals =newVals.drop('affiliation',axis=1)


# In[74]:

data_ticker = pd.read_csv('C:/Users/vvrsk/Desktop/Test- Json/tickerList.csv')


# In[98]:

p =newVals[newVals['category'].isin(pref_list)]
p['Sector']


# In[82]:

newList


# In[64]:

p


# In[120]:

#data_ticker
newListOne = []

o = data_ticker[data_ticker['Sector'].isin(p['Sector'])]
o


#for i in range(1,len(list1)):
    #if data_ticker.Industry.str.contains(list1[i]):
    #    print(list1[i] + "<==>"+ data_ticket.Industry)


# In[115]:

len(o['Symbol'])


# In[153]:

z = (o.groupby(['Sector','Industry'], as_index=False)
       .apply(lambda x: dict(zip(x.Symbol,x.Name)))
       .reset_index()
       .rename(columns={0:'compData'})
       .to_json(orient='records'))

z


# In[181]:

cols = ['Sector','Industry']
Vals =o.drop(cols,axis=1)
vals = o[cols]
print(vals.columns)
Vals.to_json('C:/Users/vvrsk/Desktop/Test- Json/final_recommendations_json2.json',orient ='records')


# In[154]:

my_final_json = z.encode('utf8')
landng_pg_data = json.loads(my_final_json)
pg_data_dump = json.dumps(landng_pg_data, indent=4, sort_keys=True)
pg_data=json.loads(pg_data_dump)
#pg_data

with open('C:/Users/vvrsk/Desktop/Test- Json/final_recommendations_json.json', 'w') as outfile:
            json.dump(pg_data, outfile)

