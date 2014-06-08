from django.core.urlresolvers import resolve
from django.test import TestCase
from app_1.views import home_page

# Byrjum á því að gera test case klasan

class HomePageTest(TestCase): 
	# Maður á alltaf að láta fallið heita það sem testið á að gera.
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page) # assert equal tekur 2 input, hvad á að gera 
								 				# og hvernig á útkoman að vera.
 

