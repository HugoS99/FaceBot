from selenium import webdriver
import random
import os
from selenium.webdriver.common.keys import Keys
from secretsP import loginEmail, password
from time import sleep


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
