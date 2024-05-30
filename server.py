import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

PORT = 8000
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        code = ''
        redirect_uri = "http://127.0.0.1:8000"
        print(f"This is self.path: {self.path}")
        code = self.path.split('?')[1].split('=')[1]
        print(f"This that code i got:{code}")


        url = "https://sandbox.orcid.org/oauth/token"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri
        }

        response = requests.post(url, headers=headers, data=data)
        print(data)
        if response.status_code == 200:
            print(f"Got an access token!!")
            data = response.json()
            # print(data)
            # print(f"Access Token: {data.get('access_token')}")  
            df = pd.read_csv('access_token_list.csv')
            df = pd.concat([df, pd.DataFrame([data])])
            df = df[['orcid','name','access_token','token_type','scope', 'refresh_token', 'expires_in']]
            df.to_csv('access_token_list.csv')
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")

Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()