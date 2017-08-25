
#Ekran Goruntusu

from selenium import webdriver
import os
cPath = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome('./chromedriver')

class ScreenResolution(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

screenSizes = [] 
screenSizes.append(ScreenResolution(1280,1024))
screenSizes.append(ScreenResolution(800,1024))

for obj in screenSizes:  
    driver.set_window_size(obj.width,obj.height)    
    driver.get('http://10.1.7.223/')
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);")
    driver.set_window_size(obj.width,height)
    driver.save_screenshot(('screen%sX%s.png' % (obj.width, height)))
driver.quit()