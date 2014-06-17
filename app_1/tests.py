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


from app_1.models import Item, List
	# database

##########################################################################################################


class ListAndItemModelsTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)




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
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
	

	
class ListViewTest(TestCase):

	def test_displays_all_items(self):
		list_ = List.objects.create()
		Item.objects.create(text='itemey 1', list=list_)
		Item.objects.create(text='itemey 2', list=list_)

		# get the url we are testing
		response = self.client.get('/lists/the-only-list-in-the-world/') #1

		# Instead of using the slightly annoying assertIn/response.content.decode() dance, 
		# Django provides the assertContains method which knows how to deal with responses 
		# and the bytes of their content.
		self.assertContains(response, 'itemey 1') #2
		self.assertContains(response, 'itemey 2')

	def test_uses_list_template(self):
		response = self.client.get('/lists/the-only-list-in-the-world/')
		# assertTemplateUsed is one of the more useful functions that the Django test client gives us. 
		self.assertTemplateUsed(response, 'list.html')

class NewListTest(TestCase):
	
	def test_saving_a_POST_request(self):
		self.client.post(
		# This is another place to pay attention to trailing slashes, incidentally. 
		# It’s /new, with no trailing slash. The convention I’m using is that URLs without 
		# a trailing slash are "action" URLs which modify the database.
		'/lists/new',
		data={'item_text': 'A new list item'}
		)
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')
	
	def test_redirects_after_post(self):
		response = self.client.post(
		'/lists/new',
		data={'item_text': 'A new list item'}
		)
		self.assertRedirects(response, '/lists/the-only-list-in-the-world/')






