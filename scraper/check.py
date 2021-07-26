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

from security.apps import read_apps_sheet

# import boto3