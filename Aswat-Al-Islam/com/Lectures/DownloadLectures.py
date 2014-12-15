__author__ = 'sandeeps'

from com.common.Utilities import Utilities
import string
from selenium.common.exceptions import NoSuchElementException


class lectures():

    def read_data(self,driver):
        lecture_table = list()
        xpath_table = '/html/body/table[2]/tbody/tr[1]/td[2]/table[2]/tbody'



        #Iterate through A-Z
        #for i in string.ascii_uppercase:
        k = 1
        #flag = 'OFF'
        #    driver.find_element_by_link_text(i).click()
        #driver.implicitly_wait(2)
        try:
            while driver.find_element_by_link_text('►').is_displayed():
                if k != 1:
                    driver.find_element_by_link_text('Page '+str(k)).click()
                download_link = driver.find_elements_by_tag_name('a')
                for i in range(0,len(download_link)):
                    if (download_link[i].text=='Download'):
                        #Following code will start downloading audios where it had been stopped
                        '''if(download_link[i].get_attribute('href').replace('%20', ' ') == "http://wr5.aswatalislam.net/data2012/Lectures//Tariq Jamil/Tariq Jamil - Tabligh Ki Ronaq (www.aswatalislam.net).mp3"):
                            flag = 'ON'
                        if(flag == 'ON' ):'''
                        Utilities().download_file(download_link[i].get_attribute('href'))
                        driver.implicitly_wait(2)
                k+=1
        except NoSuchElementException:
            print("Got NoSuchElementException at page "+str(k))

        return lecture_table

    def download_lectures(self,lecture_table,driver):
        item = lecture_table
        i = 0
        while i < len(item):
            driver.find_element_by_link_text(item[1]).click()
            driver.implicitly_wait(2)
            i+=5

