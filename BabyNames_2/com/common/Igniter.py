'''
Created on Sep 10, 2014

@author: sandeeps
'''
from com.common.Utilities import Utilities
from com import properties
from com.BabyBoyNames.ReadNames import ReadNames
import com.properties

class Igniter():
    '''def openApp(self):
        driver = serve.getmydriver()
        serve.launchapplication(driver, properties.application_url)'''

if __name__ == "__main__":
    serve = Utilities()
    driver = serve.getmydriver()


    #Launch Application
    #igniter.openFF()
    serve.launchapplication(driver,properties.application_url)

    #Read Names Table
    #ReadNames().getnames(driver)
    #Create New CSV
    serve.create_file(properties.output_path)
    #Write CSV
    serve.writeCSV(ReadNames().getnames(driver))



