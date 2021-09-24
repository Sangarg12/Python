#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os
import sys
import missingno   # module to visualize missing values 


# # Reading Data

# In[3]:


sim_df = pd.read_csv(os.getcwd()+'\\Desktop\\Python\\Small Project\\Sim\\Sim_Data_Resolved_Jan21_to_Aug21.csv')


# # Data explore

# In[5]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#Above mentioned command is to print all the inputs together in a single shell.


# In[7]:


sim_df.head(3)


# In[8]:


sim_df.shape     # to check number of rows and columns


# In[9]:


sim_df.info()

#Print a concise summary of a DataFrame.
#This method prints information about a DataFrame including the index dtype and column dtypes, 
#non-null values and memory usage.


# In[10]:


sim_df.isnull().sum()         #to check total number of missing values in columns


# # Data Cleaning

# # Dropping columns which are populated <= 60% of dataset length

# In[11]:


thresh=len(sim_df)*0.6
sim_df.dropna(how='any',thresh=thresh,axis=1,inplace=True)


# In[12]:


sim_df.shape  #checking no. of columns remains


# In[13]:


sim_df.isnull().sum()


# In[14]:


missingno.matrix(sim_df)   #visualizing missing values.


# In[ ]:


#now we have nulls in 5 columns(Labellids,Lables,Assineeidentity,Complexity,Requester Site) only, will check it later.


# In[15]:


#Resetting max column view, to see all the columns of the dataset coz by default at max 20 columns showed up.

pd.set_option('display.max_columns',40)


# In[16]:


sim_df.head(1)


# # Dropping unncessary columns

# In[17]:


#Dropping unncessary columns

sim_df.drop(columns=['TotalEffortEstimate','LocalEffortEstimate','TotalEffortRemaining','LocalEffortSpent',
                       'LocalEffortRemaining','TotalEffortSpent','EffortSpentDeprecated','LabelIds','AffectedUserCount',
                     'NextStepOwner','NextStepAction','WatcherCount','IssueId','SubTaskCount','ParentTaskCount','EditCount']
            ,axis= 1,inplace=True)


# In[18]:


# Dropping duplicates if any
sim_df.drop_duplicates(inplace=True)

#rows and columns left
sim_df.shape   


# In[19]:


sim_df.head(1)


# In[20]:


# validating data

sim_df.loc[sim_df.ShortId=='CSIA-OPS-594']


# In[21]:


list(sim_df.columns)
list(sim_df.dtypes) ## to check whether all the columns have correct data types or not


# # Converting date columns to date type, so that we can apply date method on those columns

# In[22]:


sim_df['ResolvedDate']=pd.to_datetime(sim_df['ResolvedDate'].str.replace('T',' ',))
sim_df['CreateDate']=pd.to_datetime(sim_df['CreateDate'].str.replace('T',' '))
sim_df['LastUpdatedDate']=pd.to_datetime(sim_df['LastUpdatedDate'].str.replace('T',' '))
sim_df['LastUpdatedConversationDate']=pd.to_datetime(sim_df['LastUpdatedConversationDate'].str.replace('T',' '))


# In[23]:


sim_df.head()


# In[24]:


sim_df['sim_resolved_month'] = sim_df['ResolvedDate'].dt.month_name().str.slice(stop=3)  #getting first 3 letters of month
sim_df['sim_resolved_year'] =  sim_df['ResolvedDate'].dt.year


# In[25]:


sim_df.head(2)


# In[26]:


sim_df.sim_resolved_year = sim_df.sim_resolved_year.astype('Int32')

# NOTE : sim_df.sim_resolved_year = sim_df.sim_resolved_year.astype('int32') this will give error with small 'i'


# In[28]:


sim_df['sim_create_month'] = sim_df['CreateDate'].dt.month_name().str.slice(stop=3)  #getting first 3 letters of month
sim_df['sim_create_year'] =  sim_df['CreateDate'].dt.year
sim_df.sim_create_year =   sim_df.sim_create_year.astype('Int32')


# In[29]:


sim_df.head(2)


# In[30]:


# Extracting week from the date's(Note: week start's from Monday)

sim_df['sim_create_week'] =  'Wk_'+ sim_df.CreateDate.dt.weekofyear.astype('str')
sim_df['sim_resolved_week'] =  'Wk_'+ sim_df.ResolvedDate.dt.weekofyear.astype('str')


# In[31]:


sim_df.head(2)


# # Renaming Columns and Fixing Multiple Complexity values

# In[32]:


# Column Renaming
sim_df.rename(columns ={'Complexity (string)':'Complexity','Requester Site (string)':'Requester_Site'},inplace=True)


# In[33]:


list(sim_df.columns)


# In[34]:


list(sim_df['Complexity'].unique())  #Checking unique values


# In[35]:


# Creating map Dict for complexity values

map_var = {'0':'Zero','Zero':'Zero','2':'Easy','Easy':'Easy','4':'Medium','Medium':'Medium','Hard':'Hard','8':'Hard','16':'Hard','32':'Hard'}


# In[36]:


# mapping map dict to values to change them in desired form

sim_df['Complexity']=sim_df['Complexity'].map(map_var)


# In[37]:


list(sim_df['Complexity'].unique())


# # Vlooking up for analyst site and manager from seperate file

# In[38]:


Analyst_map = pd.read_excel(os.getcwd() + '\\Desktop\\Python\\Small Project\\Sim\\Analyst map file.xlsx')


# In[39]:


Analyst_map.sort_values(by=['AssigneeIdentity'],ascending=True).head(10)


# In[40]:


sim_df= pd.merge(sim_df,Analyst_map,on='AssigneeIdentity',how='left')


# In[41]:


sim_df.head(2)


# In[42]:


list(sim_df.columns)


# # Modeling data into meaningfull information

# In[43]:


A=sim_df.groupby(['AssigneeIdentity'])    # Grouping the dataset by assignee


# In[44]:


A


# In[45]:


Total_Sim_resolved_till_now = A[['ShortId']].count()      # Couting how many sims has been assigned to analyst


# In[46]:


Total_Sim_resolved_till_now


# In[47]:


Total_Sim_resolved_till_now =Total_Sim_resolved_till_now.loc[['sangarg','sbonthal','nechhabr','appereir','tapkiv']]

# Total_Sim_resolved_till_now[Total_Sim_resolved_till_now.index.isin(['sangarg','rajencho','riyamali'])]

#both will same result eithe could be used to filter out


# In[48]:


graph=Total_Sim_resolved_till_now.plot(kind='bar',title= 'No. of Sims Assigned',legend= False,figsize=(15,5))


# # Automatic Report To Your Outlook

# In[49]:


import win32com.client as win32   # importing library


# In[51]:


outlook = win32.Dispatch('Outlook.application')

for i,j in Total_Sim_resolved_till_now.itertuples():
    
    if i =='sangarg':
        
        sender  = i 
        message = """
        Hello {0},
        <br>
        <br>
        <p>
        Total {1} sims has been resolved by you till now. Good Job!
        </p>
        <br>
        Thanks & Regards,<br>
        Sandeep | Data Analyst
        """.format(i,j)
    
        email = outlook.createitem(0)
        email.To = '{}@amazon.com'.format(sender)
        email.subject = 'SIM Performance'
        email.HTMLBody = message
        #email.display()
        email.send


# In[ ]:


# #Snippet to send Email to All

# outlook = win32.Dispatch('Outlook.application')

# for i,j in Total_Sim_resolved_till_now.itertuples():
#     sender  = i 
#     message = """
#     Hello {0},
#     <br>
#     <br>
#     Total {1} sims has been resolved by you till now. Good Job!
#     <br>
#     <br>
#     Thanks & Regards,<br>
#     Sandeep | Data Analyst
#     """.format(i,j)
      
      
#     email = outlook.createitem(0)
#     email.To = '{}@amazon.com'.format(sender)
#     email.subject = 'SIM Performance'
#     email.HTMLBody = message
#     email.display()
# #         email.send


# # Data Visualization Using Matplotlib 

# In[52]:


B_df= Total_Sim_resolved_till_now
B_df.reset_index(inplace=True)
B_df


# In[54]:


plt.figure(figsize = (11,5))
plt.bar(x= B_df['AssigneeIdentity'],height=B_df['ShortId'])
plt.title('No. of Sims Resolved')
plt.xlabel('Analyst Login')
plt.ylabel('No. of Sims')
plt.tight_layout()
for i,j in Total_Sim_resolved_till_now.values:
    plt.annotate(j,(i,j),color='red',size = 16)

plt.show()


# In[ ]:


# To check any particular portion for column/dataframe which has null values

# sim_df.loc[sim_df.Labels.isnull()]


# In[ ]:




