from selenium import webdriver
import random
import os
from selenium.webdriver.common.keys import Keys
from secretsP import loginEmail, password
from time import sleep
from urllib.request import (urlretrieve)
import pathlib
import string


class FaceBot:
    # link to the current conversation
    
    url = 'addlatter'

    def __init__(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')

    def login(self):
        self.driver.get(self.url)
        sleep(1)
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[4]/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input')
        emailin.send_keys(loginEmail)
        passin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[4]/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
        passin.send_keys(password)
        button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[4]/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/button')
        button.click()

    def messagerandom(self):
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div')

        emailin.send_keys(random.choice(list(open('pick.txt'))))
        emailin.send_keys(Keys.ENTER)

    def message(self,text):
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div')

        emailin.send_keys(text)
        emailin.send_keys(Keys.ENTER)

    def messagejoke(self):
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div')

        emailin.send_keys(random.choice(list(open('shittyjokes.txt'))))
        emailin.send_keys(Keys.ENTER)

    def sendimage(self):
        sendimage = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]/div[1]/form/div/span/input')
        dirname = "C:\\Users\hugos\Documents\PhytonShit\\bot\memes"
        filename = random.choice(os.listdir(dirname))
        sendimage.send_keys(os.path.join(dirname, filename))
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div')
        emailin.send_keys('')
        emailin.send_keys(Keys.ENTER)

    def lastmessage(self):
        lastmessage = self.driver.find_element_by_xpath(
            '(/html/body//a[@data-href=\'' + self.url + '\']/div/div[2]/div[2]/span/span)[last()]').text
        print(lastmessage)
        return lastmessage

    def replay_to_last_message(self):
        message= self.lastmessage().strip()
        if message.endswith('?'):
            googleSearch= webdriver.Chrome('../chromedriver.exe')
            googleSearch.get('https://www.google.com')
            googleQuery = googleSearch.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
            googleQuery.send_keys(message)
            googleQuery.send_keys(Keys.ENTER)
            # sleep(10)
            # googleSearch.close()
            linkList = []
            links = googleSearch.find_elements_by_xpath('//div[@class=\'bkWMgd\']//a[@href]')

            for link in links:
                linkList.append(link.get_attribute('href'))

            self.message(linkList[0])
            googleSearch.quit()

    def send_google_message(self):
        message = self.lastmessage().strip()

        googleSearch = webdriver.Chrome('../chromedriver.exe')
        googleSearch.get('https://www.google.com')
        googleQuery = googleSearch.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        googleQuery.send_keys(message)
        googleQuery.send_keys(Keys.ENTER)
        googleSearch.find_element_by_xpath('/html/body/div[7]/div[3]/div[4]/div/div/div[1]/div/div/div[1]/div/div[2]/a').click()
        # sleep(10)
        # googleSearch.close()
        images = []
        imagesResult = googleSearch.find_elements_by_xpath('//img[@class="rg_i Q4LuWd tx8vtf"]')

        for image in imagesResult:
            images.append(image.get_attribute('src'))

        pathtotempfile=pathlib.Path(__file__).parent.absolute()
        filename = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        filetemp=os.path.join(pathtotempfile, filename)
        sendimage = self.driver.find_element_by_xpath(
            '//input[@data-testid=\'photo_input\']')
        urlretrieve(images[0],filetemp+'.jpg')

        sendimage.send_keys(filetemp+'.jpg')
        emailin = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div')
        emailin.send_keys('')
        emailin.send_keys(Keys.ENTER)
        #os.remove(filetemp+'.jpg')
        googleSearch.quit()
        sleep(1)
        os.remove(filetemp + '.jpg')

    def get_song_lyrics(self):
        message = self.lastmessage().strip()
        geniusWebDriver = webdriver.Chrome('../chromedriver.exe')
        geniusWebDriver.get('https://genius.com/')
        geniusInput=geniusWebDriver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input')
        geniusInput.send_keys(message)
        geniusInput.send_keys(Keys.ENTER)
        sleep(2)
        temp=geniusWebDriver.find_elements_by_xpath('//mini-song-card/a')
        temp[1].click()
        #get lyrics from website
        sleep(2)
        result=''
        liricsf=geniusWebDriver.find_elements_by_xpath('//section//p/*')
        for liric in liricsf:
            try:
                temp=result+' '+liric.text
                print(temp)
                result=temp.replace('\n','')
            except:
                print('Error on read')

        self.message(result)
        geniusWebDriver.close()