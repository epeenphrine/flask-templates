
#%%  post requestExample
import requests
dev_url = 'http://127.0.0.1:5000'
res = requests.post(f'{dev_url}/api/requestExample').content
print(res)
#%% get requestExample
import requests
dev_url = 'http://127.0.0.1:5000'
res = requests.get(f'{dev_url}/api/requestExample').content
print(res)
#%% get data
import requests
dev_url = 'http://127.0.0.1:5000'
query_string = 'somethingsomething testing'
res = requests.get(f'{dev_url}/data?{query_string}').content
print(res)
#%% get data1
import requests
dev_url = 'http://127.0.0.1:5000'
param1= 'from param 1'
param2= 'from param 2'
res = requests.get(f'{dev_url}/data1?test1={param1}?test2={param2}').content
print(res)