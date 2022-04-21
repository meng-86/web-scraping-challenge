from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    news_url = 'https://mars.nasa.gov/news'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    browser.visit(news_url)
    time.sleep(3)

    news_html = browser.html
    news_soup = bs(news_html, "html.parser")

    news_title_find = news_soup.find('div', class_="content_title")
    news_title = news_title_find.text
    # news_title.text

    news_p_find = news_soup.find('div', class_ = "article_teaser_body")
    news_p = news_p_find.text
    # news_p

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # Find image source
    html = browser.html
    soup = bs(html, 'html.parser')

    img_src = soup.find_all('img')[1]["src"]
    # Combine base url with image source to get images url
    featured_image= url + img_src
    featured_image
    # featured_image_url

    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(mars_weather_url)
    time.sleep(3)

    weather_html = browser.html

    weather_soup = bs(weather_html, "html.parser")
    # print(weathersoup.prettify())

    mars_tweets = [weather_soup.find_all('p', class_="TweetTextSize"), weather_soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")]

    for tweets in mars_tweets:
        mars_tweet = tweets

    for tweet in mars_tweet:
        if 'InSight' in tweet.text:
            mars_weather = tweet.text
            if tweet.a in tweet:
                mars_weather = mars_weather.strip(tweet.a.text)
            break
    # mars_weather

    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)

    tables = pd.read_html(mars_facts_url)
    mars_table = tables[0]
    mars_table.rename(columns={0:'Facts',1:'Value'}, inplace=True)
    # mars_table

    mars_facts = tables[0].to_html()
    # mars_facts

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)
    hemisphere_html = browser.html
    hemisphere_soup = bs(hemisphere_html, "html.parser")
    hemispheres = hemisphere_soup.find_all('a', class_="itemLink")
    # hemispheres[0].get('href')

    link_list = []
    for hemi in hemispheres:
        if hemi.get('href') not in link_list:
            link_list.append(hemi.get('href'))
    links = ['https://astrogeology.usgs.gov' + link for link in link_list]
    # links

    hemisphere_image_urls = []
    for link in links:
        url = link
        browser.visit(url)
        
        mars_html = browser.html 
        soup = bs(mars_html, "html.parser")
        
        title_text = soup.find('h2', class_="title")
        img_url = soup.find('div', class_="downloads")
        
        hemi_dict = {'title': title_text.text, 'img_url': img_url.a.get('href')}
        hemisphere_image_urls.append(hemi_dict)
    # hemisphere_image_urls

    mars_data = {
            'news_title': news_title, 
            'news_p': news_p, 
            'featured_image':featured_image, 
            'mars_facts': mars_facts,
            'hemisphere_image_urls': hemisphere_image_urls
            }

    return mars_data
