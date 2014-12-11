'''
Created on Sep 10, 2014

@author: sandeeps
'''
from selenium import webdriver
import time
import csv
import os
from com import properties

class Utilities:
    driver = webdriver.Firefox()
    output_file = ''
    testdata = []

    def getmydriver(self):
        return self.driver

    #Launch application
    def launchapplication(self,driver,url):
        driver.get(url)

    def readCSV(self):
        csvfile_path = properties.input_path
        output_path = properties.output_path

        with open(csvfile_path, 'rb') as f:
            reader = csv.reader(f)
            for i in reader:
                Utilities.testdata.append(i)

        #Create output file
        Utilities.output_file = os.path.join(output_path, "TestResultReport_" + time.strftime("%Y-%m-%d-%H%M%S", time.localtime())) + ".csv"
        with open(Utilities.output_file,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writing.writerow(['Test_case', 'Parking Lot', 'IN_time', 'IN_date', 'OUT_time', 'OUT_date', 'Actual_cost', 'Expected_cost', 'Actual_time', 'Expected_time', 'Result', 'Comments'])

        return Utilities.testdata

    def create_file(self,output_path):
        #Create output file
        Utilities.output_file = os.path.join(output_path, "BabyBoyNames_"+"A_"+ time.strftime("%Y-%m-%d-%H%M%S", time.localtime())) + ".csv"
        with open(Utilities.output_file,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writing.writerow(['Likes', 'Name', '', 'Meaning'])


    def writeCSV(self,names_table):
        with open(Utilities.output_file ,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            item = names_table
            i = 0
            while i < len(names_table):
                writing.writerow([item[i], item[i+1], item[i+2], item[i+3]])
                i = i + 4
    