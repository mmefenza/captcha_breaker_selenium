# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime, timedelta
import time
import sys
import requests
import Image
import ImageFont
import ImageDraw
import numpy as np
import skimage.morphology as morphology
import cv2
import tesseract
import string

alphabet = list(string.ascii_lowercase)

#define the profile of the selenium driver.
# we load the ads block extension to block ads on the target.

profile = webdriver.FirefoxProfile();
profile.add_extension(extension='adblock_plus.xpi')
driver = webdriver.Firefox(firefox_profile=profile)

##logout
driver.get("http://xxxx")
driver.implicitly_wait(3)
time.sleep(3)

i=1
num=0

## captcha is in an iframe and can not be accessed directily, also it changes after each request. 
##so we take a screenshot and resize it to ROI (captcha element)

driver.get_screenshot_as_file('screenshots/screenshot'+ alphabet[num] +`i`+'.png')
iframe= driver.find_element_by_xpath('//div[@id="captcha"]//div[@id="adcopy-puzzle-image"]//iframe')
location = iframe.location
size = iframe.size

im = Image.open('screenshots/screenshot'+ alphabet[num] +`i`+'.png') # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
im = im.crop((left, top, right, bottom)) # defines crop points
im.save('captchas/captcha'+ alphabet[num] +`i`+'.png') # saves new cropped image


## captcha pre-processing
img = cv2.imread('captchas/captcha'+ alphabet[num] +`i`+'.png')
ref_bg = img[img.shape[0]-10,img.shape[1]-10]
for x in range(19):
	for y in range(145):
			img[x,y][0]=ref_bg[0]
			img[x,y][1]=ref_bg[1]
			img[x,y][2]=ref_bg[2]

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((2,2),np.uint8)
sure_bg = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

#apply Tesseract OCR
cv2.imwrite('processed/processed'+ alphabet[num] +`i`+'.png',sure_bg)
api = tesseract.TessBaseAPI()
api.Init("/usr/local/share/tessdata/", "eng", tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijlkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!'")
api.SetPageSegMode(tesseract.PSM_SINGLE_BLOCK)
pixImage=tesseract.pixRead('processed/processed'+ alphabet[num] +`i`+'.png')
api.SetImage(pixImage)
text=api.GetUTF8Text()
text = text.replace('\n', ' ')

# save decoded text as image
img1 = Image.new('RGB', (img.shape[1], img.shape[0]))
d = ImageDraw.Draw(img1)
font = ImageFont.truetype("arial.ttf", 40)
d.text((3, 40), text , font=font, fill=(255, 255, 255))
img1.save('output/output'+ alphabet[num] +`i`, 'png')

## fill captcha field
elem= driver.find_element_by_xpath('//td[@id="adcopy-response-cell"]//input')
elem.send_keys(text)

##submit the decoded captcha text
submit_button = driver.find_element_by_xpath('//input[@type="submit"]')
submit_button.click()
driver.implicitly_wait(2)
time.sleep(2)


driver.close()


