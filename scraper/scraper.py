#!/usr/bin/env python3
"""
I am check
"""

import os
import pipes
import sys

import argparse
import json
import logging
import os.path
import pprint
import re
import sys
import time
import platform
import tempfile
import io
from datetime import datetime, timedelta
from difflib import context_diff
from distutils.version import LooseVersion
from ssl import SSLCertVerificationError, SSLError
from sys import exit
from urllib.error import HTTPError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

import chromedriver_binary
import feedparser

# import git
import requests
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import MaxRetryError
from apps import read_apps_sheet
#from apps import implicit
from apps import explicit

# So I can do import from "security." whether running from main or imported into Sphinx
# No clue if I need this for this script
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Read from sheets
# Remember https://console.developers.google.com/?authuser=0&project=checkauthorizeds-1597348139916

chrome_options = Options()

# Checks to see if the user has the chrome binary
if platform.system() == "Windows":
    script_os = "Windows"
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
else:
    print("Error no chrome binary located in: C:\\ProgramFiles\\Google\\Chrome\\Application\\chrome.exe")


# Run main script
if __name__ == "__main__":
    # Not sure if i need to define range_name and apps_spreadsheet_id here
    # Or in read_apps_sheet()
    range_name = 'Scraper!A2:Q'
    # Not sure what to do with apps_spreadsheet_id here
    # Currently just a placeholder
    apps_spreadsheet_id = []
    # link to the spreadsheet
    google_sheets_url = 'https://docs.google.com/spreadsheets/d/1WOFjlrt_pqgJBcKPF18gJOaVS8lZrp6uUUT8C5oYrp4/edit?pli=1#gid=0'
# Calls Authentication function
#implicit()
explicit()

read_apps_sheet(apps_spreadsheet_id, range_name, google_sheets_url)





