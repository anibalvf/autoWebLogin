from selenium import webdriver
# import time
from selenium.webdriver.chrome.options import Options

def getOptions():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.page_load_strategy = 'normal'
    return chrome_options

def getDriver():
    chrome_options = getOptions()
    driver = webdriver.Chrome('driver/chromedriver.exe',chrome_options=chrome_options)
    driver.get('https://alumnos.escuelaartegranada.com/')
    return driver

def putUser(usuario,driver):
    mBox = driver.find_element_by_xpath('//*[@id="login"]/div[2]/form/div[1]/input')
    mBox.send_keys(usuario)#poner el usuario

def putPass(password,driver):
    mBox = driver.find_element_by_xpath('//*[@id="login"]/div[2]/form/div[2]/input')
    mBox.send_keys(password)#poner la contraseña

def clickEntrar(driver):
    driver.find_element_by_xpath('//*[@id="login"]/div[2]/form/div[4]/button').click()

def eagLogin():
    usuario = ""
    password = ""

    driver = getDriver()
    # time.sleep(2)
    
    putUser(usuario,driver)
    putPass(password,driver)
    
    clickEntrar(driver)