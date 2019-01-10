
#%%
import requests
import pandas as pd
from pandas.io.json import json_normalize
import json
import datetime
import matplotlib.pyplot as plt

#%%
pocket_api = requests.post('https://getpocket.com/v3/oauth/request',
                           data = {'consumer_key':'82708-fda3a381ec1a3dfbbd5fb633',
                                   'redirect_uri':'https://google.com'})

#%%
pocket_api.status_code 

#%%
pocket_api.text
request_token=PASTE-YOUR-REQUEST-TOKEN-HERE&amp;amp;amp;amp;amp;amp;amp;amp;amp;redirect_uri=https://getpocket.com/connected_applications