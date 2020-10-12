#!/usr/bin/python3
import lxml
import requests

source1 = 'https://store.steampowered.com/explore/new/'
source2 = 'https://euw.op.gg/summoner/userName=420%20Marenscope'

html = requests.get(source2)
doc = lxml.html.fromstring(html.content)

tree = doc.xpath('//html/body/div[3]/div[3]/div/div/div[1]/div[3]/div[1]/span/text()')

for x in tree:
    print(x)
