import requests
import pandas as pd
import argparse
from helper.get_latest_access_token import get_latest_access_token


def add_orcid_work(orcid, token, fname):
    # crafting the request from arguments
    url = f'https://api.sandbox.orcid.org/v3.0/{orcid}/work'
    data = open(fname, 'rb').read()
    auth_code = 'Bearer ' + token
    headers = {
        'Content-type': 'application/vnd.orcid+xml',
        'Authorization': auth_code
    }

    response = requests.post(url, headers=headers, data=data)
    # print(f"response.headers.items:{response.headers.items()['Location']}")
    # print(response.status_code)
    # print(f"This is response.content:{response.content}")

    if response.status_code == 201: # Assuming a 201 status indicates successful creation/update
        location_header = response.headers.get('Location')  # Safely get the Location header
        if location_header:
            put_code = location_header.split('/')[-1]  # Split by '/' and take the last part
            print("PUT-CODE:", put_code)  
        else:
            print("Location header not found in response.")
        # for key, value in response.headers.items():
        #     print(f"{key}: {value}")
    # else:
    #     if response.status_code==401:
    #         df = pd.read_csv("access_token_list.csv")
    #         mask = df['access_token'] == token
    #         df = df[~mask]
    #         df = df[['orcid','name','access_token','token_type','scope', 'refresh_token', 'expires_in']]
    #         df.to_csv('access_token_list.csv')
    #         print("Removed an expired access token!")

def main():
    # parser for cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--orcid", help="ORCID ID")
    parser.add_argument("--fname", help="File name")
    parser.add_argument("--token", help="Authentication token")
    args = parser.parse_args()

    orcid = args.orcid
    token = args.token
    fname = args.fname

    orcid = "0009-0001-1269-3022"
    token = get_latest_access_token(orcid, "access_token_list.csv")
    fname = "work_add.xml"
    add_orcid_work(orcid, token, fname)

if __name__=="__main__":
    main()
