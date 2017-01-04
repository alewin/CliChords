#!/usr/bin/python3
# coding=utf-8
# -*- coding: utf-8 -*-
# TODO clean code + add color to chords


import re
import sys
import requests
from lxml import objectify, etree
from lxml.html import tostring
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def search_tabs(query):
    tabs = None
    url = "http://app.ultimate-guitar.com/search.php?search_type=title&page=1&iphone=1&value=%s"
    tabs_xml = requests.get(url % query)
    if tabs_xml.status_code == 200:
        tabs = objectify.fromstring(tabs_xml.text.encode('utf-8'))
    return tabs


def get_tab(taburl):
    tab = requests.get(taburl).text
    tab = re.sub('\\r|\\t|<pre>|<span class="line_end">|<span>|</span>|<i>|</i>|</pre>|', "", tab).encode('utf-8') # .encode avoids UnicodeEncodeError
    tab = str(tab).replace("\\n", "\n").replace("[ch]","").replace("[/ch]","")
    return tab


def show_tab(tab):
    print("------------ START TAB --------------")
    print(tab)
    print("------------- END TAB ---------------")
    return tab


def main():
    print(bcolors.WARNING + """
               ______  _  _   ______  _                       _
              / _____)| |(_) / _____)| |                     | |
              | /      | | _ | /      | | _    ___    ____  _ | |  ___
              | |      | || || |      | || \  / _ \  / ___)/ || | /___)
              | \_____ | || || \_____ | | | || |_| || |   ( (_| ||___ |
               \______)|_||_| \______)|_| |_| \___/ |_|    \____|(___/
        """+ bcolors.ENDC)

    if len(sys.argv) > 1:
        tabs = search_tabs(sys.argv[1])
        if not tabs:
            print(bcolors.FAIL + "No tab found"+ bcolors.ENDC)
            exit()
        tab = get_tab(tabs.result[0].get('url'))
    else:
        search = input(bcolors.WARNING + "Please enter artist name or song >> "+ bcolors.ENDC)
        tabs = search_tabs(search)
        if len(tabs.result) == 0:
            print(bcolors.FAIL + "No tab found"+ bcolors.ENDC)
            exit()
        for i, tab in enumerate(tabs.result):
            print(str(i) + ") " + tabs.result[i].get("artist") + " - " + tabs.result[i].get("name") + " | " + tabs.result[i].get("type") + " | " + tabs.result[i].get("rating"))

        search = int(input(bcolors.WARNING + "Select song >> "+ bcolors.ENDC))
        taburl = tabs.result[search].get("url")
        tab = get_tab(taburl)
    show_tab(tab)


if __name__ == "__main__":
    main()
