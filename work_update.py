import requests
from helper.get_latest_access_token import get_latest_access_token
import argparse
# curl -i -H 'Content-type: application/vnd.orcid+xml' -H 'Authorization: Bearer d746ad28-3369-4eba-81af-705a9ef699b3' -d '@work_update.xml' -X PUT 'https://api.sandbox.orcid.org/v3.0/0009-0003-7578-3214/work/1931647'


def update_orcid_work(token, orcid, put_code):
    url = f'https://api.sandbox.orcid.org/v3.0/{orcid}/work/{put_code}'
    data = open("work_update.xml", 'rb').read()
    headers = {
        'Content-type': 'application/vnd.orcid+xml',
        'Authorization': f'Bearer {token}'
    }

    response = requests.put(url, headers=headers, data=data)

    if response.status_code == 200:  
        print("Work updated successfully!")
        # for key, value in response.headers.items():
        #     print(f"{key}: {value}")
    else:
        print("Error updating work:", response.status_code)
        print(response)

def main():
    # A parser for the option of passing the arguments from the command line
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--orcid", required=True, help="ORCID ID")
    # parser.add_argument("--fname", required=True, help="File name of the XML data to update with")
    # parser.add_argument("--putcode", required=True, help="PUT-CODE of the work to update")
    # parser.add_argument("--token", required=True, help="Authentication token")

    # args = parser.parse_args()
    # orcid = args.orcid


    orcid = "0009-0001-1269-3022"  
    put_code = "1931647"
    token = get_latest_access_token(orcid, 'access_token_list.csv')
    update_orcid_work(token, orcid, put_code)

if __name__=="__main__":
    main()


