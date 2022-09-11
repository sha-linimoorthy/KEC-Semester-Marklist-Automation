
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager   
import time
import pandas as pd


url="https://docs.google.com/forms/d/e/1FAIpQLSfnA-QyI6-Xzp2pNG8L6OWiriPAeabuiTii7HuHapgSCpwbSQ/viewform?vc=0&c=0&w=1&flr=0&gxid=-8203366"

df=pd.read_excel(r"C:\Users\HP\Documents\New Folder\Odform.xlsx")

web=webdriver.Chrome(ChromeDriverManager().install())
web.get(url)
time.sleep(2)

for i in df.index:
    
    entry=df.loc[i]
    name=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    name.send_keys(entry['Name'])
    time.sleep(1)
    
    
    roll_no=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    roll_no.send_keys(i+1)
    time.sleep(1)

      
    mail=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    mail.send_keys(entry['Mail'])
    time.sleep(1)
    
    
    odtype=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div")
    odtype.click()
    time.sleep(1)    
    
    colname=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea")
    colname.send_keys(entry['College'])
    time.sleep(1)
    
    eventname=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea")
    eventname.send_keys(entry['Event'])
    time.sleep(1)
    
    submit=web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()
    time.sleep(1)
    web.back()
    web.refresh()    
    time.sleep(2)
    
    
    