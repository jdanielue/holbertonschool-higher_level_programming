#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
   html = r.read()
print ("Body response:", end='\n')
print('\t- type: ', type(html))
print('\t- content:', html)
print('\t- utf8 content: ', html.decode('utf-8'))
