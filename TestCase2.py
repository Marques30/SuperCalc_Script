from selenium import webdriver
import unittest

def Calc(y):

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

	cleariElem = browser.find_element_by_name('clear')
	cleariElem.click()

	onelElem = browser.find_element_by_name('one')
	onelElem.click()

	eightElem = browser.find_element_by_name('eight')
	eightElem.click()

	divElem = browser.find_element_by_name('div')
	divElem.click()

	secElem = browser.find_element_by_name('two')
	secElem.click()

	equalElem = browser.find_element_by_name('DoIt')
	equalElem.click()

	clearyElem = browser.find_element_by_name('clear')
	clearyElem.click()

	threeElem = browser.find_element_by_name('three')
	threeElem.click()

	subElem = browser.find_element_by_name('minus')
	subElem.click()

	fourElem = browser.find_element_by_name('four')
	fourElem.click()

	equatElem = browser.find_element_by_name('DoIt')
	equatElem.click()

	clearmElem = browser.find_element_by_name('clear')
	clearmElem.click()

	sevenElem = browser.find_element_by_name('seven')
	sevenElem.click()

	sixElem = browser.find_element_by_name('six')
	sixElem.click()

	nineElem = browser.find_element_by_name('nine')
	nineElem.click()

	multElem = browser.find_element_by_name('times')
	multElem.click()

	fiveElem = browser.find_element_by_name('five')
	fiveElem.click()

	zeroElem = browser.find_element_by_name('zero')
	zeroElem.click()

	equaElem = browser.find_element_by_name('DoIt')
	equaElem.click()

	clearElem = browser.find_element_by_name('clear')
	clearElem.click()
