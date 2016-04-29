#!/usr/bin/python3
# coding=utf-8

import urllib.request
from lxml import etree
from lxml.html import fromstring, tostring
import re
import signal
import sys


def signal_handler(signal, frame):
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def get_html(url):
	html = ""
	try:
		response = urllib.request.urlopen(url)
		html = response.read()
		response.close()
	except urllib.error.HTTPError as err:
		print("Tab not found")
		main()
	finally:
		return html



def parse_html(html, url, xpt):
    if html == "":
        html = get_html(url)
    tree = etree.HTML(html)
    elements = tree.xpath(xpt)
    return elements


def search_tabs(query):
    tabs = []
    url = "http://www.ultimate-guitar.com/search.php?search_type=title&order=&value=%s" % (query)
    rows = parse_html("", url, "//table[contains(@class, 'tresults')]//tr[not(contains(., 'Artist :'))][not(contains(., 'tab pro'))][not(contains(., 'guitar pro'))]")
    for row in rows:
        try:
            tab_type = row[3][0].text
            tab_title = row[1][0].text
            tab_url = row[1][0].attrib["href"]
            tab_artist = tab_url.split("/")[4].replace('_', ' ').title()
            tab = {'title': tab_title, 'artist': tab_artist, 'link': tab_url, 'type': tab_type}
        except:
            tab = {'title': "", 'artist': "", 'link': ""}
        tabs.append(tab)
    return tabs


def read_tab(url):
    tab = ""
    song = parse_html("", url, '//pre[contains(@class, "js-tab-content")]')
    tab = str(tostring(song[0]))[30:]
    tab = re.sub("<span>|</span>|<i>|</i>|</pre>", "", tab)
    return tab



def main():
    search = input("Please enter artist name or song >> ")
    tabs = search_tabs(search)
    for i, tab in enumerate(tabs):
      try:
        print(str(i) + ") " + tab["artist"] + " - " + tab["title"] + " | " + tab["type"])
      except: pass
    search = int(input("Select song >> "))
    selected = tabs[search]
    tab = read_tab(selected["link"])

    tab = str(tab).replace("\\n", "\n").replace("\\r","").replace("\\'","'")
    print("------------ START TAB --------------")
    print(tab)
    print("------------- END TAB ---------------")


if __name__ == "__main__":
    main()
