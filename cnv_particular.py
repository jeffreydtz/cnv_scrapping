from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from helium import *
import time
from lxml import html 
import requests
from bs4 import BeautifulSoup

chromedriver.install()
def socios(x):
    nueva_lista = []
    
    for i in x:
        if i != False:
            info = []
            for j in i:
                driver = start_chrome(j,headless=True)

                time.sleep(5)
                try:
                    # find the td elements with column attribute = "3"
                    razon_socio = driver.find_element_by_xpath('//*[@id="1gridformedit17053"]/div/div[4]/div/table/tbody/tr/td[4]')
                    convenio_socio = driver.find_element_by_xpath('//*[@id="1gridformedit17053"]/div/div[4]/div/table/tbody/tr/td[5]')
                    # extract the text content of each td element
                    # close the webdriver instance
                    info.append({"Razon social socio ": razon_socio.text, " Fecha de suscripcion socio ": convenio_socio.text}) 
                except:
                    info.append("No posee contrato")
                driver.quit()
            nueva_lista.append(info)
        else:
            nueva_lista.append("No posee contratos")
    
    return(nueva_lista)
    
def socios2(x): 
        if x != False:
            info = []
            for j in x:
                driver = start_chrome(j,headless=True)

                time.sleep(5)
                try:
                    # find the td elements with column attribute = "3"
                    razon_socio = driver.find_element_by_xpath('//*[@id="1gridformedit17053"]/div/div[4]/div/table/tbody/tr/td[4]')
                    convenio_socio = driver.find_element_by_xpath('//*[@id="1gridformedit17053"]/div/div[4]/div/table/tbody/tr/td[5]')
                    # extract the text content of each td element
                    # close the webdriver instance
                    info.append({"Razon social socio ": razon_socio.text, " Fecha de suscripcion socio ": convenio_socio.text}) 
                except:
                    info.append("No posee contrato")
                driver.quit()
            return info
        else:
            return ("No posee contratos")
    