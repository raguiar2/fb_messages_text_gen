#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import json
INBOX_DIR = "messages/inbox"
OUTPUT_FILE = 'output.txt'


# In[4]:


test_dir = os.listdir("messages/inbox")[-10]


# In[6]:


os.listdir(INBOX_DIR + "/" + test_dir)


# In[10]:


def process_file(f, subdir, filename):
    with open(subdir + "/" + filename) as file:
        data = file.read()
        json_data = json.loads(data)
        for message in json_data['messages']:
            if message['sender_name'] == 'Rui Aguiar' and 'content' in message:
                # deal with apostrophe characters
                ascii_message = message['content'].encode('ascii', 'ignore').decode('ascii')
                f.write(ascii_message + '\n')

def process_dir(f, directory):
    subdir = INBOX_DIR + "/" + directory
    for file_name in os.listdir(INBOX_DIR + "/" + directory):
        if file_name.startswith('message'):
            process_file(f, subdir, file_name)
            

def process_dirs():
    f = open("output.txt","a")
    dir_names =  os.listdir("messages/inbox")
    for dir_name in dir_names:
        process_dir(f, dir_name)
    f.close()

process_dirs()


# In[ ]:





# In[ ]:





# In[ ]:




