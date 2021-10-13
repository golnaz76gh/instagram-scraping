import time, wget, os, requests, re, json,string
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def login_and_get_post_links(username_search, post_count=24):

    PATH = r"C:/Users/Golnaz/Desktop/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.instagram.com/")

    #login:
    username = driver.find_element_by_css_selector("input[name='username']")
    password = driver.find_element_by_css_selector("input[name='password']")
    username.clear()
    password.clear()
    username.send_keys("jogamo3386")
    password.send_keys("A1B2C3@")
    login = driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(5)

    #save your login info?
    notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    time.sleep(5)

    #turn on notif
    notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    time.sleep(5)

    #Search Box
    searchbox=driver.find_element_by_css_selector("input[placeholder='Search']")
    searchbox.clear()
    searchbox.send_keys(username_search)
    searchbox.send_keys(Keys.ENTER)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)

    #get links of posts
    post = 'https://www.instagram.com/p/'
    post_links = []
    driver.get('https://www.instagram.com/'+ username_search)
    while len(post_links) < post_count:
        links = [a.get_attribute('href')
                 for a in driver.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0,200)"
        driver.execute_script(scroll_down)
    else:
        driver.stop_client()
        return post_links


def get_post_details(link):

    PATH = r"C:/Users/Golnaz/Desktop/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    time.sleep(3)
    img = driver.find_element_by_tag_name('img')
    img_result = img.get_attribute('src')
    caption = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "C4VMK", " " ))]').text
    try:
        views = driver.find_element_by_class_name('vcOH2').text
        post_details = {'img_link': img_result, 'Caption': caption, 'Likes': None,'Views': views}
    except:
        likes = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "zV_Nj", " " ))]').text
        post_details = {'img_link': img_result, 'Caption': caption, 'Likes': likes,'Views': None}
    return post_details

def bio(username_search):
    PATH = r"C:/Users/Golnaz/Desktop/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.instagram.com/'+ username_search + '/')
    posts_followers_following = driver.find_elements_by_class_name('g47SY')
    posts_number = posts_followers_following[0]
    followers_number = posts_followers_following[1]
    following_number = posts_followers_following[2]
    bio = driver.find_element_by_class_name('-vDIg')
    result = {
        'Post Numbers': posts_number.text,
        'Followers Number': followers_number.text,
        'Following Numbers': following_number.text,
        'Bio': bio.text
        }
    return result

    
