from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

def init_browser(): 

    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

#scrape func
def scrape():

    browser = init_browser()

#MARS NEWS

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news = soup.find("div", class_ = "list_text")
    news_title = news.find("div", class_ = "content_title").text
    news_p = news.find("div", class_ = "article_teaser_body").text

# MARS SPACE IMAGES
    
    browser.visit("https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA17200")
    html = browser.html
    soup = BeautifulSoup(html,"html.parser")
    y = soup.find('img', class_ = 'main_image')["src"]
    complete_url = "https://www.jpl.nasa.gov"
    featured_image_url = complete_url + y

#MARS Facts
#read html
    mars_info = pd.read_html("https://space-facts.com/mars/")  
#df 
    mars_info = pd.DataFrame(mars_info[0])
#columns
    mars_info.columns = ["Description", "Mars"]  
#changing to html string
    mars_facts_s = mars_info.to_html()


# MARS Hemispheres

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    hemi_title_image = [ ]
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemi = soup.find_all("div", class_ = "item")

    for h in hemi:
        title = h.find("h3").text
        ima_url = h.a["href"]
        astro_link = "https://astrogeology.usgs.gov/"
        image_link = astro_link + ima_url
        response = requests.get(image_link)
        soup = BeautifulSoup(response.text, "html.parser")
        final_url = soup.find("img", class_ = "wide-image")["src"]
        hemisphere_img_url = astro_link + final_url
    
        hemi_title_image.append({"title" : title, 
                       "img_url" : hemisphere_img_url})

# dictionary: 5 componets

    scrape_data = {
        "news_title":  news_title, 
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts_s": mars_facts_s,
        "hemi_title_image" : hemi_title_image 
    }

    browser.quit()

    return scrape_data

#print (scrape())


