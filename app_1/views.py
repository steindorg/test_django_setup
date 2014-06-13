from django.shortcuts import render
from django.http import HttpResponse

# Render function is a django function that takes a request as its first paramenter and 
# the name of the template to render as its second parameter. Django will automatically 
# search folders called templates in my apps directories then it builds an httpresponse based on the template. 

def home_page(request):
	#if request.method == 'post':
	#	return HttpResponse(request.post['item_text'])
	

			# Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
	return render(request, 'home.html', {
		#'new_item_text': request.POST['item_text'],
		# ný útfærsla 
								# hvad er ad gerast herna 
								# get(key[, default])¶
								# Return the value for key if key is in the dictionary, else default. 
								# If default is not given, it defaults to None, so that this method never raises 
								# a KeyError.
								# QueryDict.get(key, default)

								# 
		'new_item_text': request.POST.get('item_text',''),	
	})
	# return HttpResponse('<html><title>To-Do lists</title></html>')
