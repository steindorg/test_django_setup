
# extendet functional test 

# Here we have new methods that we use to get data, methods that
# selenium provides to examine web pages

# find_element_by_tag_name, find_element_by_id, 
# find_elements_by_tag_name( returns several elements )

# We also use send_keys which is seleniums way of typing into input elements


# the any function
# list comprehensions and generator expressions.
# similar to map and filter in scheme and SML
# List comprehensions provide an alternative to using the built-in map() 
# and filter() functions. map(f, S) 
# is equivalent to [f(x) for x in S] while filter(P, S) is equivalent to [x for x in S if P(x)].
# These functions return a list.

# Python3 List comprehension
# [x**2 for x in (1, 2, 3)] -> returns a list


# example
# Note that there is a difference between list comprehension returning a list
# squared_set = [square_it(x) for x in x_set]
# and returning a generator that you can iterate over it:
# squared_set = (square_it(x) for x in x_set)


from django.test import LiveServerTestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(LiveServerTestCase):  #1

	def setUp(self):  #2
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):  
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])


	def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
		self.browser.get(self.live_server_url)


		# she notices the page title and header mention to-do-list
		self.assertIn('To-Do', self.browser.title)  
		
		header_text = self.browser.find_element_by_tag_name('h1').text
		
		self.assertIn('Start a new To-Do list', header_text)
		
		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')


		# When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy peacock feathers" as an item in a
        # to-do list table
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		# assertRegex is a helper function from unittest that checks 
		#whether a string matches a regular expression. We use it to check that our new REST-ish design has been implemented
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		


		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		# Now a new user, Francis, comes along to the site.

		## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()


		# Francis visits the home page.  There is no sign of Edith's
        # list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)


        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)


        # Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)




        # Again, there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)


		# Satisfied, they both go back to sleep
       

