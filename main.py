import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller

data = []
keyboard = Controller()
class readcsv:
    with open('sample.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
def Buy(i):
    # Targetting the Country Tab
    Webelement_Country=driver.find_element_by_id("react-select-2-input").send_keys(data[i]['Country'])
    # Targetting the Validity Tab
    Webelement_Validity=driver.find_element_by_id("valid-since-input").send_keys(data[i]['Validity Begins'])
    # Targetting the License Tab
    Webelement_Country=driver.find_element_by_class_name('order-0.flex-grow-1').send_keys(data[i]['License Plate'])
    # Targetting and checking
    Webelement_Power = driver.find_element_by_id("alternative_fuel_type_checkbox_0")
    if data[i]['Powered by'] == "Natural Gas":
        Webelement_Power.click()
        Webelement_NatGas = driver.find_element_by_id("natural_gas_radio_array_option_0").click()
    if data[i]['Powered by'] == "Biomethane":
        Webelement_Power.click()
        Webelement_NatGas = driver.find_element_by_id("bio_methane_radio_array_option_0").click()

    if data[i]['Type of Vignette'] == "Annual":
        Webelement_Vig=WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='1Y2021_0']"))
        )
        button = driver.find_element_by_xpath("//input[@id='1Y2021_0']")
        driver.execute_script("arguments[0].click();", button)

    if data[i]['Type of Vignette'] == "30-day":
        Webelement_Vig=WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='30D2021_0']"))
        )
        button = driver.find_element_by_xpath("//input[@id='1Y2021_0']")
        driver.execute_script("arguments[0].click();", button)

    if data[i]['Type of Vignette'] == "10-day":
        Webelement_Vig=WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='10D2021_0']"))
        )
        button = driver.find_element_by_xpath("//input[@id='1Y2021_0']")
        driver.execute_script("arguments[0].click();", button)

driver = webdriver.Chrome(executable_path='C:\Program Files\Python310\Scripts\chromedriver.exe')
driver.get("https://edalnice.cz/en/bulk-purchase/index.html")
Webelement_Button_NewBatch = driver.find_element(By.CLASS_NAME,'kit__button.btn.btn-danger')
Webelement_Button_Continue = driver.find_element(By.CLASS_NAME,'kit__button.w-100.btn.btn-primary')

for i in range(len(data)):
    Buy(i)
    Webelement_Button_NewBatch.click()
