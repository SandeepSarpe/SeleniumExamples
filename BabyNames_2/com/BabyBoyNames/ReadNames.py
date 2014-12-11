__author__ = 'sandeeps'

from com.common.Utilities import Utilities
import string
from selenium.common.exceptions import NoSuchElementException

class ReadNames():

    def getnames(self,driver):
        names_table = list()
        xpath_table = '//*[@id="wrap"]/div[6]/div[2]/table/tbody'

        driver.find_element_by_link_text('Indian Baby Names').click()

        #Iterate through A-Z
        for i in string.ascii_uppercase:
            k = 1
            driver.find_element_by_link_text(i).click()
            driver.implicitly_wait(2)
            try:
                while driver.find_element_by_link_text('  Next »').is_displayed():
                    if k!=1:
                        driver.find_element_by_link_text(str(k)).click()
                    temp_table = driver.find_element_by_xpath(xpath_table).text.split('\n')
                    for j in temp_table:
                        names_table.append(j)
                    driver.implicitly_wait(2)
                    k+=1
            except NoSuchElementException:
                print("")

        return names_table

