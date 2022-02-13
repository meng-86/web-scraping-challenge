{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "38476245",
   "metadata": {},
   "source": [
    "## Preparations \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "25589a18",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'selenium'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1185442926.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpymongo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0msplinter\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mBrowser\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask_pymongo\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m# license that can be found in the LICENSE file.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0msplinter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbrowser\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mBrowser\u001b[0m  \u001b[1;31m# NOQA\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\browser.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0murllib3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexceptions\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommon\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexceptions\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msplinter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirefox\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mWebDriver\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mFirefoxWebDriver\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'selenium'"
     ]
    }
   ],
   "source": [
    "# Dependencies \n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1a245ab0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/2533973684.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mexecutable_path\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'executable_path'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m'chromedriver'\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mbrowser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBrowser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'chrome'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mexecutable_path\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheadless\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Browser' is not defined"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86e46b81",
   "metadata": {},
   "source": [
    "# NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d3e71acd",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1951560050.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# URL of page to be scraped\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'https://mars.nasa.gov/news/'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mhtml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1c029c29",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'soup' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1784904566.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Retrieve the latest news title\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mnews_title\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'content_title'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;31m# Retrieve the latest news paragraph\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mnews_p\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'rollover_description_inner'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mnews_title\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'soup' is not defined"
     ]
    }
   ],
   "source": [
    "# Retrieve the latest news title\n",
    "news_title=soup.find_all('div', class_='content_title')[0].text\n",
    "# Retrieve the latest news paragraph\n",
    "news_p=soup.find_all('div', class_='rollover_description_inner')[0].text\n",
    "news_title\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33293a4c",
   "metadata": {},
   "source": [
    "## JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "75f58774",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/151669565.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mjpl_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"https://www.jpl.nasa.gov\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mjpl_image_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mjpl_image_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "jpl_url=\"https://www.jpl.nasa.gov\"\n",
    "jpl_image_url=\"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(jpl_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "332c9d0e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1859073184.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# HTML object\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mhtml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;31m# Parse HTML\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"html.parser\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# Retrieve image url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "# HTML object\n",
    "html=browser.html\n",
    "# Parse HTML\n",
    "soup=bs(html,\"html.parser\")\n",
    "# Retrieve image url\n",
    "image_url=soup.find_all('article')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a604ba40",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'soup' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/3610715106.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mimage_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'article'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'style'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mimage_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mimage_url\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'soup' is not defined"
     ]
    }
   ],
   "source": [
    "image_url=soup.find('article')['style']\n",
    "image_url=image_url.split(\"'\")[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a23ec5b9",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'image_url' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1869310298.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfeatured_image_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mjpl_url\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mimage_url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mfeatured_image_url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'image_url' is not defined"
     ]
    }
   ],
   "source": [
    "featured_image_url=jpl_url+image_url\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd100009",
   "metadata": {},
   "source": [
    "## Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a58ad07b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/3356234666.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Scrape Mars weather from twitter\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'https://twitter.com/marswxreport?lang=en'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mhtml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "# Scrape Mars weather from twitter\n",
    "url='https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "693803d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'soup' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/537877060.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Retrieve the latest tweet from Mars weather twitter\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mmars_weather\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'p'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmars_weather\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'soup' is not defined"
     ]
    }
   ],
   "source": [
    "# Retrieve the latest tweet from Mars weather twitter\n",
    "mars_weather=soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c1dfd3b",
   "metadata": {},
   "source": [
    "## Mars Fact"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e2beef0a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/3068442862.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Scrape Mars facts from https://space-facts.com/mars/\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'https://space-facts.com/mars/'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mtables\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_html\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mtables\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "# Scrape Mars facts from https://space-facts.com/mars/\n",
    "url='https://space-facts.com/mars/'\n",
    "tables=pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f81c2eb9",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tables' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1269644799.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmars_fact\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtables\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mmars_fact\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmars_fact\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrename\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;34m\"Profile\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;34m\"Value\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"raise\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mmars_fact\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mset_index\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Profile\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mmars_fact\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'tables' is not defined"
     ]
    }
   ],
   "source": [
    "mars_fact=tables[0]\n",
    "mars_fact=mars_fact.rename(columns={0:\"Profile\",1:\"Value\"},errors=\"raise\")\n",
    "mars_fact.set_index(\"Profile\",inplace=True)\n",
    "mars_fact"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "10fdf25f",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'mars_fact' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/4171539531.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfact_table\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmars_fact\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_html\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mfact_table\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'mars_fact' is not defined"
     ]
    }
   ],
   "source": [
    "fact_table=mars_fact.to_html()\n",
    "fact_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3b9e43c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'fact_table' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/24886630.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfact_table\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'\\n'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfact_table\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'fact_table' is not defined"
     ]
    }
   ],
   "source": [
    "fact_table.replace('\\n','')\n",
    "print(fact_table)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cd5fff6",
   "metadata": {},
   "source": [
    "## Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5d78d585",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'browser' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1322024599.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0musgs_url\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'https://astrogeology.usgs.gov'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mhtml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'browser' is not defined"
     ]
    }
   ],
   "source": [
    "# Scrape Mars hemisphere title and image\n",
    "usgs_url='https://astrogeology.usgs.gov'\n",
    "url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "cc8550ef",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'soup' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/3954930111.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Extract hemispheres item elements\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mmars_hems\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'collapsible results'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mmars_item\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmars_hems\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'item'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mhemisphere_image_urls\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'soup' is not defined"
     ]
    }
   ],
   "source": [
    "# Extract hemispheres item elements\n",
    "mars_hems=soup.find('div',class_='collapsible results')\n",
    "mars_item=mars_hems.find_all('div',class_='item')\n",
    "hemisphere_image_urls=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a27d3fc6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'mars_item' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/573111299.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Loop through each hemisphere item\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mitem\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmars_item\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[1;31m# Error handling\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[1;31m# Extract title\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'mars_item' is not defined"
     ]
    }
   ],
   "source": [
    "# Loop through each hemisphere item\n",
    "for item in mars_item:\n",
    "    # Error handling\n",
    "    try:\n",
    "        # Extract title\n",
    "        hem=item.find('div',class_='description')\n",
    "        title=hem.h3.text\n",
    "        # Extract image url\n",
    "        hem_url=hem.a['href']\n",
    "        browser.visit(usgs_url+hem_url)\n",
    "        html=browser.html\n",
    "        soup=bs(html,'html.parser')\n",
    "        image_src=soup.find('li').a['href']\n",
    "        if (title and image_src):\n",
    "            # Print results\n",
    "            print('-'*50)\n",
    "            print(title)\n",
    "            print(image_src)\n",
    "        # Create dictionary for title and url\n",
    "        hem_dict={\n",
    "            'title':title,\n",
    "            'image_url':image_src\n",
    "        }\n",
    "        hemisphere_image_urls.append(hem_dict)\n",
    "    except Exception as e:\n",
    "        print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "20446031",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'news_title' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/3350463593.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Create dictionary for all info scraped from sources above\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m mars_dict={\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;34m\"news_title\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mnews_title\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;34m\"news_p\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mnews_p\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;34m\"featured_image_url\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mfeatured_image_url\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'news_title' is not defined"
     ]
    }
   ],
   "source": [
    "# Create dictionary for all info scraped from sources above\n",
    "mars_dict={\n",
    "    \"news_title\":news_title,\n",
    "    \"news_p\":news_p,\n",
    "    \"featured_image_url\":featured_image_url,\n",
    "    \"mars_weather\":mars_weather,\n",
    "    \"fact_table\":fact_table,\n",
    "    \"hemisphere_images\":hemisphere_image_urls\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "078d083c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'mars_dict' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4832/1364270034.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmars_dict\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'mars_dict' is not defined"
     ]
    }
   ],
   "source": [
    "mars_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146a952e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
