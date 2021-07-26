#!/usr/bin/env python3
"""
I am check
"""

import os
import pipes
import sys

# So I can do import from "security." whether running from main or imported into Sphinx
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

# Read from sheets
# Remember https://console.developers.google.com/?authuser=0&project=checkauthorizeds-1597348139916

from scraper.apps import read_apps_sheet

# Run main script
if __name__ == "__main__":
    # Not sure if this link should be here under main or not
    google_sheets_url = 'https://docs.google.com/spreadsheets/d/1WOFjlrt_pqgJBcKPF18gJOaVS8lZrp6uUUT8C5oYrp4/edit?pli=1#gid=0'

    read_apps_sheet()


