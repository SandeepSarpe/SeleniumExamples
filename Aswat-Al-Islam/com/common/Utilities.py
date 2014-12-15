'''
Created on Sep 10, 2014

@author: sandeeps
'''
from selenium import webdriver
import time
import csv
import os
from com import properties
import requests
import shutil

class Utilities:
    driver = webdriver.Firefox()
    output_file = ''
    testdata = []
    global dump

    def getmydriver(self):
        return self.driver

    #Launch application
    def launchapplication(self,driver,url):
        driver.get(url)

    def download_file(self, url):
        local_filename = url.split('/')[-1].replace('%20', ' ')
        path = properties.output_path
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(path+"\\"+local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()


