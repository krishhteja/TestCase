from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("file:///Users/krishnavaddepalli/Desktop/lsh/lsh.html") ##Update the file path here
inputElement = driver.find_element_by_id("readval")

""" Test for testisyöte"""
inputElement.send_keys('testisyöte')
driver.find_element_by_id('compute').click()
val = driver.find_element_by_id("results")
value = val.get_attribute('value')
assert value == 'TeStIsYöTe'

""" Test for num 5 on pariton"""
inputElement.clear()
inputElement.send_keys('num 5 on pariton')
driver.find_element_by_id('compute').click()
val = driver.find_element_by_id("results")
value = val.get_attribute('value')
assert value == 'NuM o On PaRiToN'

""" Test for hel 123 $# abc"""
inputElement.clear()
inputElement.send_keys('hel 123 $# abc')
driver.find_element_by_id('compute').click()
val = driver.find_element_by_id("results")
value = val.get_attribute('value')
assert value == 'HeL oEo $# AbC'

print("Success")

driver.quit()
