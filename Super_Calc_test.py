from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v1.html')

oneElem = browser.find_element_by_name('one')
oneElem.click()

plusElem = browser.find_element_by_name('plus')
plusElem.click()

fiveElem = browser.find_element_by_name('five')
fiveElem.click()

equaElem = browser.find_element_by_name('DoIt')
equaElem.click()

