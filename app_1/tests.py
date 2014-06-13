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


from django.template.loader import render_to_string

# To cut down on the repetitive nature of loading and rendering templates, 
# Django provides a shortcut function which largely automates the process: render_to_string() in django.template.loader, 
# which loads a template, renders it and returns the resulting string:


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
		
		# method : String containing the HTTP method used by the request ('GET' or 'POST')
		request.method = 'POST'
		
		# POST: A QueryDict representing form values submitted using the HTTP POST method

		request.POST['item_text'] = 'A new list item'


# 		This object is an instance of a class called HttpResponse.
		# We pass it to our home_page view, which gives us a response
		response = home_page(request)
										# HttpResponse.content
										# A bytestring representing the content, encoded from a Unicode object if necessary.
										# We use .decode() to convert the response.content bytes into a Python unicode string, 
										# which allows us to compare strings with strings, 
										# instead of bytes with bytes as we did earlier.
		self.assertIn('A new list item', response.content.decode())
		
						# Django provides a shortcut function which largely automates the process: 
						# render_to_string() in django.template.loader, 
						# which loads a template, renders it and returns the resulting string: 
						# The function takes one argument " The template name " which is the name of the template
						# that should be loaded and rendered and two optional arguments 
						# ---Second argument--- is a dictionary. A dictionary to be used as variables 
						# and values for the template’s context. This can also be passed as the second positional argument.
						# ---Third--- is Context_instance. An instance of Context or a subclass (e.g., an instance of RequestContext) 
						# to use as the template’s context. This can also be passed as the third positional argument.
		expected_html = render_to_string(
			'home.html',
			# New item text er python variable sem er declerað í töflu í htmlinu
			# The render_to_string function takes, as its second parameter, a mapping of variable names to values. 
			# We’re giving the template a variable named new_item_text, whose value is the expected item text from our POST request.
			{'new_item_text': 'A new list item'}
		)
		

		


		# expected_html = render_to_string('home.html')
		
		# we have to use the b'' syntax to compare because response.content is rawbytes and not a
		# python string which means that b '' converts whats there into a raw byte file 
		# self.assertTrue(response.content.startswith(b'<html>'))  

		# Now We use .decode() to convert the response.content bytes into a Python 
		# unicode string, which allows us to compare strings with strings, 
		# instead of bytes with bytes as we did earlier.
		self.assertEqual(response.content.decode(), expected_html) 

        
        
		self.assertIn(b'<title>To-Do lists</title>', response.content)  
		self.assertTrue(response.content.endswith(b'</html>'))
