#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html")
print("Content-Type: text/plain\n")


import cgi
import cgitb
import requests

cgitb.enable()

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1","Не задано")
text2 = form.getfirst("TEXT_2","Не задано")
text3 = form.getfirst("TEXT_3","Не задано")


text = "Name: " + text1, "Phone: " + text2, "Details: " + text3

api_token = '1203482100:AAHAavmpUxML8AvwhE1RhaHI9YpdT1PdkJ8'

requests.get(f'https://api.telegram.org/bot{api_token}/sendMessage?chat_id=-1001388999753&text={text}')

