example = {'access_token': '505977a3-a4cd-4829-8518-96ba151ece01', 
           'token_type': 'bearer', 
           'refresh_token': 'ac9c89e4-6b31-44a3-aa34-193245242b58', 
           'expires_in': 631138518, 
           'scope': '/read-limited /activities/update /person/update', 
           'name': 'Person two', 
           'orcid': '0009-0009-2409-7859'}

import pandas as pd
df = pd.read_csv('access_token_list.csv')
cols = df.columns
print(cols)