#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
    html = r.read()
print("Body response:", end='\n')
print('\t- type: {}' .format(type(html)))
print('\t- content: {}' .format(html))
print('\t- utf8 content: {}' .format(html.decode('utf-8')))
