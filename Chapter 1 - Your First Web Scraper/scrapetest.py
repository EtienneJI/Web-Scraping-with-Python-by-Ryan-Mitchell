# -*- coding: utf-8 -*-
"""
Author:     Brian Mascitello
Date:       3/6/2016
School:     Arizona State University
Website:    http://pythonscraping.com/
Book:       Web Scraping with Python by Ryan Mitchell
"""

from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())