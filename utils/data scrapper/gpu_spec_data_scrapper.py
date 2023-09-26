from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def name_cleaner(gpu_name):
    fixed = gpu_name.lower().replace('laptop', 'mobile').replace('gpu','').replace('with','').replace('design','')
    fixed.lower
    return fixed
driver = webdriver.Chrome()

url = 'https://www.techpowerup.com/gpu-specs/'

driver.get(url)

gpus = pd.read_csv('utils/data scrapper/gpu_benchmark_data.csv')

for i, gpu in gpus.iterrows():
    cleaned_name = name_cleaner(gpu[0])
    print(cleaned_name)
    search_box = driver.find_element(By.ID, 'quicksearch')
    search_box.clear()
    search_box.send_keys(name_cleaner(gpu[0]))
    time.sleep(2)
    gpu_elements = driver.find_element(By.ID, 'ajaxresults')
    gpu_scrapped = gpu_elements.find_element(By.XPATH, ".//tbody/tr[1]")
    
    GPU_CHIP = []
    RELEASED = []
    BUS = []
    MEMORY = []
    GPU_CLOCK = []
    MEMORY_CLOCK = []
    SHADERS_TMUs_ROPs = []

    print(gpu_scrapped.get_attribute('innerHTML'))
    time.sleep(10)