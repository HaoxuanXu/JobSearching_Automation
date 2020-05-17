from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


job_keywords = "data intern"
location = "chicago"

browser = webdriver.Chrome("drivers/chromedriver.exe")

browser.get("https://www.indeed.com")
job_search = browser.find_element_by_xpath('//*[@id="text-input-what"]')
location_search = browser.find_element_by_xpath('//*[@id="text-input-where"]')
find_job_button = browser.find_element_by_css_selector("#whatWhereFormId > div.icl-WhatWhere-buttonWrapper > button")
job_search.send_keys(job_keywords)
location_search.send_keys(Keys.CONTROL + "a")
location_search.send_keys(Keys.DELETE)
location_search.send_keys(location)
browser.execute_script("arguments[0].click();", find_job_button)

sort_by_date = browser.find_element_by_css_selector(
    "#resultsCol > div.resultsTop > div.secondRow > div.serp-filters-sort-by-container > span.no-wrap > a")

sort_by_date.click()
# close_popover = browser.find_element_by_css_selector("#popover-x > a > svg > g > path")
close_popover = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             '#popover-x > a > svg > g > path')))
close_popover.click()



job_title = browser.find_elements_by_xpath('//*[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')[0]
print(job_title)