#!/usr/bin/env python
# coding: utf-8

# In[2]:


import plotly as pt
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\ivan2\\results.csv') ### reading data from csv file 
print(df)
df.info()


# In[3]:


df['date'] = df['date'].apply(lambda x: int(str(x)[:4]))
print(df['date']) ### edit fisrt collumn for more convenient usage.
print(df)         ### Final dataframe 


# In[4]:


### Info about home_score goals

print('Info about home_score goals')
print('Median:', df['home_score'].median())
print('Mean:', df['home_score'].mean())
print('Standart deviation:', df['home_score'].std())
print('Minimal value:', df['home_score'].min())
print('Maximal value:', df['home_score'].max())


# In[5]:


### Info about away_score goals

print('Info about away_score goals')
print('Median:', df['away_score'].median())
print('Mean:', df['away_score'].mean())
print('Standart deviation:', df['away_score'].std())
print('Minimal value:', df['away_score'].min())
print('Maximal value:', df['away_score'].max())


# In[6]:


### Info about dates of matches

print('Info about dates of matches')
print('Median:', df['date'].median())
print('Mean:', df['date'].mean())


# In[7]:


# Sorting tournaments, cities and years.

num_tournaments = df["tournament"].value_counts()[:10]
num_city = df["city"].value_counts()[:10]
num_matches = df["date"].value_counts() ### number int.matches per year. 
print(num_tournaments)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(num_city)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(num_matches)


# In[8]:


###Most popular tournaments 
plt.plot(num_tournaments,"g-x",markersize=10,markeredgecolor="purple")
plt.xticks(rotation=70)


# In[9]:


### Most visited cities.
plt.plot(num_city,"g-x",markersize=10,markeredgecolor="red",color='blue')
plt.xticks(rotation=60)


# In[10]:


### Data about years
plt.figure(figsize=(10,6))
df.groupby("date")["home_team"].count()[:-1].plot.area(alpha=0.6,color="green")
plt.xlabel("Years")
plt.ylabel("Number of matches played")
plt.title("Rise of football matches per year")


# In[11]:


###Scoring results
home_goals = df['home_score'].sum()
away_goals = df['away_score'].sum()
all_goals = home_goals + away_goals
print('All home_score goals ever:',home_goals)
print('All away_score goals ever:',away_goals)
print('All goals ever:',all_goals)
scoring = df.groupby('home_team')[['home_score','away_score']].sum()
scoring['total'] = scoring['home_score'] + scoring['away_score']
scoring = scoring.sort_values('total', ascending = False)
scoring = scoring[:10]
scoring.plot(kind = 'bar')
plt.xticks(rotation=60)


# In[12]:


#### Number of all matches for countries.
away=df["away_team"].value_counts()
home=df["home_team"].value_counts()
for x in away.index:
    if x not in home.index:
        home[x]=0
for x in home.index:
    if x not in away.index:
        away[x]=0        
total=home+away
total_mtch = total.sort_values(ascending=False)[:25].to_frame(name="All matches")
total_mtch.plot(kind='barh',color='green')


# As we can see , football has been popular through the whole period because it reached from 1 official internation match per year to more than 1200 matches per year. There was only one decline during the WWII , while all other time this trend was increasing. Moreover, we can analyze that most successful teams are from Europe and Southern America. There is a strong relation between number of wins and total played matches. 
