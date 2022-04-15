#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install google-api-python-client


# In[3]:


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


# In[4]:


scopes = ['https://www.googleapis.com/auth/calendar']


# In[19]:


flow = InstalledAppFlow.from_client_secrets_file("client.json", scopes=scopes)


# In[21]:


credentials = flow.run_console()


# In[22]:


import pickle


# In[23]:


pickle.dump(credentials, open("token.pkl", "wb"))


# In[24]:


credentials = pickle.load(open("token.pkl", "rb"))


# In[25]:


service = build("calendar", "v3", credentials=credentials)


# In[26]:


result = service.calendarList().list().execute()


# In[27]:


result['items'][0]


# In[29]:


calendar_id = result['items'][0]['id']


# In[30]:


result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()


# In[31]:


result['items'][0]


# In[ ]:




