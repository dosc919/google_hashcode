import os
import requests
from bs4 import BeautifulSoup
import numpy as np

fo = open(os.path.join(os.path.abspath('./athlets'), filename), "r")
html_doc = fo.read()