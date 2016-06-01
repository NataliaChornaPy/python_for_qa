# Having data file with web site clients clients.json, find clients who don't have access to web service (site uses Basic Authentication).
import requests
from requests.auth import HTTPBasicAuth
import json
import ssl
import urllib3

ENDPOINT = 'https://python-for-qa.herokuapp.com/login'
USER = 'user'
PASSWORD = 'passwd'

def main():
    data_file2=open('clients.json')
    data2=json.load(data_file2)
    for b in data2:
        # print b['name']
        USER=b['name']
        PASSWORD=b['password']
        # print PASSWORD
        response = requests.get(ENDPOINT, auth=HTTPBasicAuth(USER, PASSWORD))
        if  not response:
            print "Can not to connect"
        # print response.status_code


if __name__ == '__main__':
    main()