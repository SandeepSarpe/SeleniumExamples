'''
Created on Sep 10, 2014

@author: sandeeps
'''
from com.common.Utilities import Utilities
from com import properties
from com.Lectures.DownloadLectures import lectures
import com.properties
import urllib

class Igniter():
    '''def openApp(self):
        driver = serve.getmydriver()
        serve.launchapplication(driver, properties.application_url)'''

if __name__ == "__main__":
    serve = Utilities()
    driver = serve.getmydriver()
    urllib


    #Launch Application
    #igniter.openFF()
    serve.launchapplication(driver,properties.application_url)
    '''download_link = driver.find_elements_by_tag_name('a')
    for i in range(0,len(download_link)):
        if (download_link[i].text=='Download'):
            print(download_link[i].text)
            download_link[i].click()
            download_link[i].get_attribute('href')'''
    #Read Lectures
    lectures().read_data(driver)
    #Download lectures
    #lectures().download_lectures(lectures,driver)

