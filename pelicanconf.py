#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = '真🐟'
SITENAME = '廢文記錄生活'
SITEURL = 'localhost'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh-tw'

# Basic settings
DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Themes
THEME = 'theme/pelican-themes/bulrush'

# URL settings
ARTICLE_URL = PAGE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = PAGE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html'

# # Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True