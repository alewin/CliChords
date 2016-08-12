#!/usr/bin/python3
# coding=utf-8
# -*- coding: utf-8 -*-
# TODO clean code


import re
import sys
import requests
from lxml import objectify, etree
from lxml.html import tostring
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)


def search_tabs(query):
    tabs = None
    url = "http://app.ultimate-guitar.com/search.php?search_type=title&page=1&iphone=1&value=%s"
    tabs_xml = requests.get(url % query)
    if tabs_xml.status_code == 200:
        tabs = objectify.fromstring(tabs_xml.text.encode('utf-8'))
    return tabs


def get_tab(taburl):
    tab = requests.get(taburl).text
    tab = re.sub('<span class="line_end">|<span>|</span>|<i>|</i>|</pre>|', "", tab)
    tab = str(tab).replace("\\n", "\n").replace("\\r", "").replace("\\t", "").replace("\\'", "'").replace("[ch]","").replace("[/ch]","")
    return tab


def show_tab(tab):
    print("------------ START TAB --------------")
    print(tab)
    print("------------- END TAB ---------------")
    return tab


def main():
    print("""
               ______  _  _   ______  _                       _
              / _____)| |(_) / _____)| |                     | |
              | /      | | _ | /      | | _    ___    ____  _ | |  ___
              | |      | || || |      | || \  / _ \  / ___)/ || | /___)
              | \_____ | || || \_____ | | | || |_| || |   ( (_| ||___ |
               \______)|_||_| \______)|_| |_| \___/ |_|    \____|(___/
        """)

    if len(sys.argv) > 1:
        tabs = search_tabs(sys.argv[1])
        if not tabs:
            print("No tab found")
            exit()
        tab = get_tab(tabs.result[0].get('url'))
    else:
        search = input("Please enter artist name or song >> ")
        tabs = search_tabs(search)
        if len(tabs.result) == 0:
            print("No tab found")
            exit()
        for i, tab in enumerate(tabs.result):
            print(str(i) + ") " + tabs.result[i].get("artist") + " - " + tabs.result[i].get("name") + " | " + tabs.result[i].get("type"))

        search = int(input("Select song >> "))
        taburl = tabs.result[search].get("url")
        tab = get_tab(taburl)
    show_tab(tab)


if __name__ == "__main__":
    main()
