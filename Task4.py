#!/usr/bin/env python
# coding: utf-8

# # EDA(Exploratory data analysis) using olympics dataset

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


athletes=pd.read_csv("D:/olympic/athlete_events.csv")
regions=pd.read_csv("D:/olympic/noc_regions.csv")


# In[3]:


athletes.head()


# In[4]:


regions.head()


# In[5]:


#JOin the dataframes
athletes_df=athletes.merge(regions,how="left",on="NOC")
athletes_df.head()          
                


# In[6]:


athletes_df.shape


# In[7]:


#Data cleaning
#column name consistent
athletes_df.rename(columns={'region':'Region','notes':'Notes'}, inplace=True)


# In[8]:


athletes_df.head()


# In[9]:


athletes_df.info()


# In[10]:


athletes_df.describe()


# In[11]:


#check null values
nan_values=athletes_df.isna()
nan_columns=nan_values.any()
nan_columns


# In[12]:


#total number of null values for above 6 columns
athletes_df.isnull().sum()


# In[13]:


#India details
athletes_df.query('Team=="India"').head(5)


# In[14]:


#Japan details
athletes_df.query('Team=="Japan"').head(5)


# In[15]:


#Top 10 countreis
top_10_countries=athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
top_10_countries


# In[16]:


#Top 10 countries
plt.figure(figsize=(12,6))
plt.title=("Overall Participation by Country")
sns.barplot(x=top_10_countries.index, y=top_10_countries, palette="Set2")


# In[17]:


#Age distribution of athletes

plt.figure(figsize=(12,6))
plt.title=('Age Distribution of the athletes')
plt.xlabel("Age")
plt.ylabel("Number of participants")
plt.hist(athletes_df.Age, bins=np.arange(10,80,2),color='orange', edgecolor="white")


# In[18]:


#winter olympics
winter_sports=athletes_df[athletes_df.Season=="Winter"].Sport.unique()
winter_sports


# In[19]:


#summer olympics
summer_sports=athletes_df[athletes_df.Season=="Summer"].Sport.unique()
summer_sports


# In[20]:


#count for male and female athletes
gender_counts=athletes_df.Sex.value_counts()
gender_counts


# In[21]:


#pie plot for male and female athletes
plt.figure(figsize=(2,6))
#lt.title("Gender Distribution")
plt.pie(gender_counts,labels=gender_counts.index,autopct="%1.1f%%",startangle=150, shadow=True)
        


# In[45]:


#Total medals
athletes_df.Medal.value_counts()


# In[23]:


#total number of female athletes in each olympics
female_participants=athletes_df[(athletes_df.Sex=="F")& (athletes_df.Season=="Summer")][['Sex','Year']]
female_participants=female_participants.groupby('Year').count().reset_index()
female_participants.tail()


# In[24]:


womenOlympics=athletes_df[(athletes_df.Sex=="F")& (athletes_df.Season=="Summer")]


# In[25]:


sns.set(style="darkgrid")
plt.figure(figsize=(20,10))
sns.countplot(x="Year", data=womenOlympics, palette="Spectral")



# In[26]:


#line graph
part=womenOlympics.groupby("Year")["Sex"].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()


# In[47]:


#GOld medal athletes
gold_medals=athletes_df[(athletes_df.Medal=="Gold")]
gold_medals.head()


# In[28]:


sporting_event=gold_medals['Sport'][gold_medals['Age']>60]
sporting_event


# In[35]:


#Gold medal from each country
gold_medals.Region.value_counts().reset_index(name="Medal").head(5)


# In[36]:


# Gold medals per country

totalGoldMedals=gold_medals.Region.value_counts().reset_index(name="Medal").head(6)
g=sns.catplot(x="index",y="Medal", data=totalGoldMedals,
             height=5, kind="bar", palette="rocket")
g.despine(left=True)
g.set_x_labels("Top 5 countries")
g.set_y_lables("Number of Medals")


# In[39]:


#Rio olympics

max_year=athletes_df.Year.max()
print(max_year)

team_names=athletes_df[(athletes_df.Year==max_year) & (athletes_df.Medal=="Gold")].Team

team_names.value_counts().head(10)


# In[40]:


sns.barplot(x=team_names.value_counts().head(20), y=team_names.value_counts().head(20).index)

plt.ylabel(None);
plt.xlabel("Countrywise Medals for the year 2016");


# In[41]:


not_null_medals=athletes_df[(athletes_df["Height"].notnull()) & (athletes_df["Weight"].notnull())]


# In[43]:


plt.figure(figsize=(12,10))
axis=sns.scatterplot(x="Height", y="Weight", data=not_null_medals, hue="Sex")
#plt.title("Height vs Weight of Olympic Medalists")


# In[ ]:




