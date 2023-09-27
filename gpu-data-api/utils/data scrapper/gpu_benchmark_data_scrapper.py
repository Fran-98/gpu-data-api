from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()

url = 'https://www.videocardbenchmark.net/high_end_gpus.html'

driver.get(url)

chart = driver.find_element(By.CLASS_NAME, 'chartlist')
#print(chart.get_attribute('innerHTML'))
gpus_elements = chart.find_elements(By.XPATH, ".//li[contains(@id,'rk')]")

#print(gpus_elements[0].get_attribute('innerHTML'))
GPU = []
SCORE = []
PRICE = []

for i in gpus_elements:
    #print(i.get_attribute('innerHTML'))
    GPU.append(i.find_element(By.XPATH, './/span[@class="prdname"]').text)
    SCORE.append(i.find_element(By.XPATH, './/span[@class="count"]').text)
    PRICE.append(i.find_element(By.XPATH, './/span[@class="price-neww"]').text.replace('*',''))
    print(f'added {GPU[-1]}, score of {SCORE[-1]}, ${PRICE[-1]}')

df = pd.DataFrame({
    'gpuName': GPU,
    'averageScore': SCORE,
    'price': PRICE
})

df = df.sort_values(by='averageScore')
print(df)
df.to_csv('gpu-data-api/utils/data scrapper/gpu_benchmark_data.csv', index=False)