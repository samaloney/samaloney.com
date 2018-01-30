#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shane Maloney'
SITENAME = 'samaloney'
# SITEURL = 'http://127.0.0.1:8000'
SITEURL = 'http://samaloney.com'

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

PAGE_ORDER_BY = 'page-order'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AVATAR = 'https://pbs.twimg.com/profile_images/879771897650479104/IW1qXFlU_400x400.jpg'
SIDEBAR_DIGEST = 'Solar Physics, Programming, Technology'
TWITTER_USERNAME = 'samaloney'

# Blogroll
LINKS = (('SunPy', 'http://sunpy.org/'),
         ('xrayvision', 'http://github.com/sunpy/xrayvision'),
         ('TCD Astro', 'http://www.tcd.ie/Physics/research/themes/astrophysics/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/samaloney'),
          ('github', 'https://github.com/samaloney'),
          ('twitter', 'https://twitter.com/samaloney'))


DISPLAY_FOOTER = False

STATIC_PATHS = ['pages/images', 'extra/favicon.ico', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME' : {'path': 'CNAME'}
}

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Home', SITEURL),
			 ('Blog', SITEURL + '/category/blog.html'),)

PAGES = True



DEFAULT_PAGINATION = False

# TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ["pelican_publications"]


READERS = {'html': None}

THEME = '../pelican-blue'
