# Ekran Goruntusu
# Alican Çamlıbel 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
cPath = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Firefox() #For FireFox
#driver = webdriver.Chrome('./chromedriver')  For Chrome

class ScreenResolution(object):
    def __init__(self, width, height,name):
        self.width = width
        self.height = height
        self.name = name

screenSizes = []
screenSizes.append(ScreenResolution(1024,600,'10inch Notebook')) #10" Notebook
screenSizes.append(ScreenResolution(1024,768,'12inch Notebook')) #12" Notebook
screenSizes.append(ScreenResolution(1280,800,'13inch Notebook')) #13" Notebook
screenSizes.append(ScreenResolution(1366,768,'15inch Notebook')) #15" Notebook
screenSizes.append(ScreenResolution(1440,900,'19inch Notebook')) #19" Notebook
screenSizes.append(ScreenResolution(1600,900,'20inch Notebook')) #20" Notebook
screenSizes.append(ScreenResolution(1680,1050,'22inch Notebook')) #22" Notebook
screenSizes.append(ScreenResolution(1920,1080,'23inch Notebook')) #23" Notebook
screenSizes.append(ScreenResolution(1920,1200,'24inch Notebook')) #24" Notebook
screenSizes.append(ScreenResolution(800,480,'Kindle Fire HD 7inch')) #Kindle Fire HD 7"
screenSizes.append(ScreenResolution(960,600,'Asus Nexus 7')) #Asus Nexus 7
screenSizes.append(ScreenResolution(1024,600,'Kindle Fire')) #Kindle Fire
screenSizes.append(ScreenResolution(1024,768,'Apple iPad')) #Apple iPad
screenSizes.append(ScreenResolution(1024,600,'Samsung Galaxy Tab 7inch')) #Samsung Galaxy Tab 7"
screenSizes.append(ScreenResolution(1280,800,'Kindle Fire HD 8.9inch')) #Kindle Fire HD 8.9"
screenSizes.append(ScreenResolution(1280,800,'Samsung Galaxy Tab'))
screenSizes.append(ScreenResolution(1366,1024,'Apple iPad Pro')) #Apple iPad Pro
screenSizes.append(ScreenResolution(1440,1024,'Microsoft Surface Pro')) #Microsoft Surface Pro
screenSizes.append(ScreenResolution(176,220,'Motorola RAZR V3m')) #Motorola RAZR V3m
screenSizes.append(ScreenResolution(240,320,'Motorola RAZR V8')) #Motorola RAZR V8
screenSizes.append(ScreenResolution(320,240,'Blackberry 8300')) #Blackberry 8300
screenSizes.append(ScreenResolution(320,480,'Apple iPhone 3/4')) #Apple iPhone 3/4
screenSizes.append(ScreenResolution(320,533,'Samsung Galaxy S2')) #Samsung Galaxy S2
screenSizes.append(ScreenResolution(320,568,'Apple iPhone 5')) #Apple iPhone 5
screenSizes.append(ScreenResolution(320,568,'Lg G3-5')) #LG G3-5
screenSizes.append(ScreenResolution(320,568,'Samsung Galaxy S3-7')) #Samsung Galaxy S3-7
screenSizes.append(ScreenResolution(320,568,'Apple iPhone 6/7')) #Apple iPhone 6/7
screenSizes.append(ScreenResolution(320,568,'Apple iPhone 6/7 Plus')) #Apple iPhone 6/7 Plus


for obj in screenSizes:  
    driver.set_window_size(obj.width,obj.height)    
    driver.get('')
    height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(obj.width,height)
    driver.save_screenshot(('screen%sX%s-%s.png' % (obj.width, height,obj.name)))

driver.quit()