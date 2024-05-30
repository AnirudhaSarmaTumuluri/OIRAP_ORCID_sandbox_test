import requests
from helper.get_latest_access_token import get_latest_access_token

def delete_orcid_work(token, orcid, put_code):

    headers = {
        'Content-type': 'application/vnd.orcid+xml',
        'Authorization': f'Bearer {token}'
    }

    url = f'https://api.sandbox.orcid.org/v3.0/{orcid}/work/{put_code}'

    with open('work_update.xml', 'rb') as file:  # Read XML file in binary mode
        data = file.read()

    response = requests.delete(url, headers=headers, data=data)

    if response.status_code == 204:
        print("Work deleted successfully!")
    else:
        print(f"Error deleting work: {response.status_code} - {response.text}")


orcid_id = "0009-0001-1269-3022"
orcid_token = get_latest_access_token(orcid_id, "access_token_list.csv")
work_put_code = "1909249"

delete_orcid_work(orcid_token, orcid_id, work_put_code)
