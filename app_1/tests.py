from django.test import TestCase

# Byrjum á því að gera test case klasan

class smokeTest(TestCase): 

	def test_bad_maths(self):
		self.assertEqual(1+1, 3) # assert equal tekur 2 input, hvad á að gera 
								 # og hvernig á útkoman að vera.
 
# Create your tests here.
