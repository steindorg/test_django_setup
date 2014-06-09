##########################################################################################################								 


									 # url resolver utility functions
									 # resolve is used for resolving URL paths to the corresponding view functions.
from django.core.urlresolvers import resolve
						

						# we use the TestCase class
						# augmented version of the standard unittest.TestCase, 
						# with some additional Django-specific features
from django.test import TestCase


from django.http import HttpRequest
						# We create an HttpRequest object, which is what 
						# Django will see when a user’s browser asks for a page.




						# What function is that? It’s the view function we’re 
						# going to write next, which will actually return the HTML we want. 
						# You can see from the import that we’re planning to store it in lists/views.py.
from app_1.views import home_page


##########################################################################################################

# Byrjum á því að gera test case klasan

class HomePageTest(TestCase): 
	
	# Maður á alltaf að láta fallið heita það sem testið á að gera.
	def test_root_url_resolves_to_home_page_view(self):
		
		# Can we resolve the URL for the root of the site (“/”) to a particular view function we’ve made?
		found = resolve('/')
		
		# Can we make this view function return some HTML which will get the functional test to pass?
		self.assertEqual(found.func, home_page) # assert equal tekur 2 input, hvad á að gera 
								 				# og hvernig á útkoman að vera.
 

	def test_home_page_returns_correct_html(self):
  		# We create an HttpRequest object, which is what Django 
  		# will see when a user’s browser asks for a page.
		request = HttpRequest() 
		
		# This object is an instance of a class called HttpResponse.
		# We pass it to our home_page view, which gives us a response
		response = home_page(request)
		
		# we have to use the b'' syntax to compare because response.content is rawbytes and not a
		# python string which means that b '' converts whats there into a raw byte file 
		self.assertTrue(response.content.startswith(b'<html>'))  
        
        
		self.assertIn(b'<title>To-Do lists</title>', response.content)  
		self.assertTrue(response.content.endswith(b'</html>'))
