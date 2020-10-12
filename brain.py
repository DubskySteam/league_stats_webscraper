#!/usr/bin/python3s
from bs4 import BeautifulSoup

given_server = ['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'ru', 'tr']
given_userid = input('UserID: ')
source_html = 'https://' + given_server[2] +'.op.gg/summoner/userName=' + given_userid

html = BeautifulSoup('source_html', 'html.parser')

html.find_all(class_='Level tip tpd-delegation-uid-1')
