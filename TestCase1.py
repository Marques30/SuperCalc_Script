from selenium import webdriver

def function(SJ):

	if (SJ) >= 1034: 

		browser = webdriver.Firefox()
		browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v1.html')

		oneElem = browser.find_element_by_name('four')
		oneElem.click()

		secElem = browser.find_element_by_name('two')
		secElem.click()

		addElem = browser.find_element_by_name('plus')
		addElem.click()

		thridElem = browser.find_element_by_name('five')
		thridElem.click()

		equElem = browser.find_element_by_name('DoIt')
		equElem.click()

		multElem = browser.find_element_by_name('times')
		multElem.click()

		secrElem = browser.find_element_by_name('two')
		secrElem.click()

		secdElem = browser.find_element_by_name('two')
		secdElem.click()

		equaElem = browser.find_element_by_name('DoIt')
		equaElem.click()

	elif (SJ):
		return False