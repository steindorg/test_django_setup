
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
		self.browser.get('http://localhost:8000')


		# she notices the page title and header mention to-do-list
		self.assertIn('To-Do', self.browser.title)  
		
		header_text = self.browser.find_element_by_tag_name('h1').text
		
		self.assertIn('Your To-Do list', header_text)
		
		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')


		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		
		

		

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		


		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.
		self.fail('Finish the test!')  #6
		# Satisfied, she goes back to sleep

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8

