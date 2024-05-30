import requests
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
from helper.get_latest_access_token import get_latest_access_token


def get_work_put_codes(orcid_id, access_token):
    
    headers = {
        "Accept": "application/vnd.orcid+xml",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"https://api.sandbox.orcid.org/v3.0/{orcid_id}/works"
    response = requests.get(url, headers=headers)

    if response.status_code == 200 or response.status_code==201:
        root = ET.fromstring(response.content)
        ns = {
    'common': 'http://www.orcid.org/ns/common',
    'activities': 'http://www.orcid.org/ns/activities',
    'work': 'http://www.orcid.org/ns/work'
}
        data = []
        for group in root.findall('activities:group', ns):
            for summary in group.findall('work:work-summary', ns):
                title = summary.find('work:title/common:title', ns).text
                last_modified_date = summary.find('common:last-modified-date', ns).text
                put_code = summary.attrib['put-code']
                print(f"{title}:{put_code}")
                path = summary.attrib['path']
                external_ids = summary.findall('common:external-ids/common:external-id', ns)
                for external_id in external_ids:
                    external_id_type = external_id.find('common:external-id-type', ns).text
                    external_id_value = external_id.find('common:external-id-value', ns).text
                    external_id_url = external_id.find('common:external-id-url', ns).text
                    external_id_relationship = external_id.find('common:external-id-relationship', ns).text
                    data.append({
                        'title': title,
                        'last_modified_date': last_modified_date,
                        'put_code': put_code,
                        'path': path,
                        'external_id_type': external_id_type,
                        'external_id_value': external_id_value,
                        'external_id_url': external_id_url,
                        'external_id_relationship': external_id_relationship
                    })

        df = pd.DataFrame(data)
        print(df)

    else:
        raise Exception(f"Error retrieving works: {response.status_code} - {response.text}")


parser = argparse.ArgumentParser()
parser.add_argument("--orcid", required=True, help="ORCID ID to fetch works for")
args = parser.parse_args()
orcid_id = args.orcid
access_token = get_latest_access_token(orcid_id, 'access_token_list.csv')

try:
    put_codes = get_work_put_codes(orcid_id, access_token)
    print(put_codes)
except Exception as e:
    print(f"An error occurred: {e}")
