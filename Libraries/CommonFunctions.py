'''
__author__ = gaurav kumar
version = 0.1
date= 10/08/2018
This file contains common functions which are related to Demo Framework
'''

from selenium import webdriver
import subprocess, datetime
import os, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image, ImageGrab
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class CommonFunctions:
    '''
        __author__ = gaurav kumar
        version = 0.1
        date= 10/05/2018
        Comment: This function will take screenshot of Complete Screen
        '''
    def failurecapturescreen(self):
        self.fileSaveLocation=''
        if os.name == 'nt':
            self.fileSaveLocation = 'C:/Test_Results/screenshots'
        elif os.name == 'posix':
            self.fileSaveLocation =  os.path.expanduser('~/Desktop/Test_Results/screenshots')

        filename = ""
        try:
            if not os.path.exists(self.fileSaveLocation):
                os.makedirs(self.fileSaveLocation)

            filename = os.path.join(self.fileSaveLocation, (self.gettimestamp() + ".png"))
            print("Taking Screenshot... file name: " + str(filename))
            if os.name == "nt":
                try:
                    img = ImageGrab.grab()
                    img = img.resize((800, 640), Image.ANTIALIAS)
                    img.save(filename)
                    img.close()
                except Exception, e:
                    print("Failed to take screenshot on Win, " + str(e))
            else:
                cmd = ["screencapture", filename]
                subprocess.call(cmd)

                retryCount = 0
                while (not os.path.exists(filename)) and retryCount < 10:
                    time.sleep(2)
                    retryCount += 1
                if not os.path.exists(filename):
                    raise Exception("Couldn't Capture Mac screenshot")

                # Compress screenshot to save space
                subprocess.call(["sips", "-z", "640", "800", filename])

            time.sleep(1)
        except Exception, e:
            print("Exception in failurecapturescreen " + str(e))
        return os.path.basename(filename)

    '''
            __author__ = gaurav kumar
            version = 0.1
            date= 10/08/2018
            Comment: This function will provide Current date and take for naming screenshot
    '''
    def gettimestamp(self):
        timestampInSecs = time.time()
        timestamp = datetime.datetime.fromtimestamp(timestampInSecs).strftime('%Y-%m-%d-%H-%M-%S-%f')
        return timestamp

    '''
               __author__ = gaurav kumar
               version = 0.1
               date= 10/08/2018
               Comment: This is decorator function
       '''
    def screenshot(function):
        def screenshot_exception(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except:
                self.failurecapturescreen()
                error = "There was an exception in  "
                error += function.__name__
                raise Exception(error)

        return screenshot_exception

    '''
               __author__ = gaurav kumar
               version = 0.1
               date= 10/8/2018
               Comment: This is will create the Driver instance
    '''
    @screenshot
    def driver_instance(self, browser):
        self.driver = ""

        if browser.lower().strip()== "chrome" :
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
            print("Driver initiated for Chrome")
        elif browser.lower().strip()=="firefox" :
            capabilities = webdriver.DesiredCapabilities().FIREFOX
            capabilities["marionette"] = True
            binary = FirefoxBinary()
            self.driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities,executable_path ='geckodriver.exe')
            # self.driver = webdriver.Firefox(executable_path ='geckodriver.exe')
            print("Driver initiated for Firefox")
        else :
            print("Browser Name not specified")
        self.driver.maximize_window()
        return self.driver

    '''
                   __author__ = gaurav kumar
                   version = 0.1
                   date= 10/8/2018
                   Comment: This is will open url in driver instance
    '''
    @screenshot
    def open_app(self,url):
        print url
        self.driver.get(url)
        print "Open url in driver instance "

    '''
                       __author__ = gaurav kumar
                       version = 0.1
                       date= 10/08/2018
                       Comment: This is will check on  Home Screen presence of textbox
        '''

    @screenshot
    def is_search_box_present(self):
        elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME, "q")))
        if elem:
            print "Search Box is Present "
            return True
        else:
            print "Search Box is not Present "
            return False

    '''
                       __author__ = gaurav kumar
                       version = 0.1
                       date= 10/08/2018
                       Comment: This is will open url in driver instance
        '''

    @screenshot
    def close_app(self):
        self.driver.quit()
        print "quit driver instance "

    '''
                          __author__ = gaurav kumar
                          version = 0.1
                          date= 10/08/2018
                          Comment: This is will check on  Home Screen presence of textbox
           '''

    @screenshot
    def is_image_link_present(self):
        elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Images")))
        if elem:
            print "Image Link is Present "
            return True
        else:
            print "Image Link is not Present "
            return False

    '''
                              __author__ = gaurav kumar
                              version = 0.1
                              date= 10/08/2018
                              Comment: This is will click on  image link and search images and validate initial result count =100
               '''

    @screenshot
    def search_images(self,text):
        elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Images")))
        elem.click()
        self.search_field = self.driver.find_element(By.ID,"lst-ib")
        self.search_field.send_keys(text)
        self.search_field.submit()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "rg_ic.rg_i")))
        results=self.driver.find_elements(By.CLASS_NAME, "rg_ic.rg_i")
        if len(results)== 100:
            print "The count of images results is coming 100 as expected"
            return True
        else:
            print "The count of images results is not coming 100 as expected"
            return False

    '''
                                __author__ = gaurav kumar
                                version = 0.1
                                date= 10/08/2018
                                Comment: This is vlidate the search on home page
                 '''

    @screenshot
    def search_text(self, text):
        self.search_field = self.driver.find_element(By.NAME, "q")
        self.search_field.send_keys(text)
        self.search_field.submit()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "g")))
        results = self.driver.find_elements(By.CLASS_NAME, "rc")
        for element in results:
            if not text.lower() in element.text.lower():
                print "The serach text: "+ text+" is not coming in result as expected : " + element.text
                return False
            else:
                print element.text
        return True
