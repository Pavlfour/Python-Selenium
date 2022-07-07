from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def func_1():
    try:
        account_sid = ""  #HIDDEN
        auth_token = ""  #HIDDEN

        driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver1.implicitly_wait(40)
        driver1.get("https://wizardgui.avis.com/wizardgui/ui/wizard.jsf")
        driver1.find_element(by=By.NAME, value="username").send_keys("") #HIDDEN
        driver1.find_element(by=By.NAME, value="PASSWORD").send_keys("" + Keys.ENTER) #HIDDEN
        driver1.find_element(by=By.XPATH, value='//select[@name="stationForm:locationMenu"]/option[@value="HER"]').click()
        driver1.find_element(by=By.NAME, value='stationForm:okBtn').click()
        time.sleep(10)
        driver1.find_element(by=By.XPATH, value='//*[@id="footerForm:footerSettingButton"]').click()   #settings button
        driver1.find_element(by=By.XPATH, value='//*[@id="userManagement:userManageView:reportingHeaderForm:reportingType"]/option[@value="object:8226"]').click()
        driver1.find_element(by=By.XPATH, value='//*[@id="userManagement:userManageView:reportingHeaderForm:search"]/span').click()
        time.sleep(10)
        for elem1 in driver1.find_elements(by=By.XPATH, value='//*[@id="userManagement:userManageView:reportingContainer:reportingForm:RoDataTable"]/div[2]/div[2]/div/span'):
            x=elem1
        a = x.text

        while True:
            time.sleep(20)
            #n1 = datetime.datetime.now().strftime("%H:%M")
            driver1.find_element(by=By.XPATH, value='//*[@id="userManagement:userManageView:reportingHeaderForm:search"]/span').click()
            for elem2 in driver1.find_elements(by=By.XPATH, value='//*[@id="userManagement:userManageView:reportingContainer:reportingForm:RoDataTable"]/div[2]/div[2]/div/span'):
                y=elem2
            b = y.text
            if a != b:
                client = Client(account_sid, auth_token)
                #c = str(int(b.split()[4]) - int(a.split()[4]))
                client.messages.create(
                    body="🟥(" +b+ ") ",
                    from_='+14012273171',
                    to='' #HIDDEN
                )
                a = b
    except Exception:
        driver1.quit()
        time.sleep(5)
        func_1()

func_1()
