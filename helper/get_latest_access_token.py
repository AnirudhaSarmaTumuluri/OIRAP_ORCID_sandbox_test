import pandas as pd

def get_latest_access_token(orcid, csv_file):
    df = pd.read_csv(csv_file)
    token = df[df['orcid'] == orcid]['access_token'].iloc[-1]
    return token

# Usage
# orcid = '0009-0001-1269-3022'
# latest_token = get_latest_access_token(orcid)
# print(latest_token)