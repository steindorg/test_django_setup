from django.shortcuts import render


# Render function is a django function that takes a request as its first paramenter and 
# the name of the template to render as its second parameter. Django will automatically 
# search folders called templates in my apps directories then it builds an httpresponse based on the template. 

def home_page(request):
	return render(request, 'home.html')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
