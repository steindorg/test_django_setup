from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_1.models import Item

# Render function is a django function that takes a request as its first paramenter and 
# the name of the template to render as its second parameter. Django will automatically 
# search folders called templates in my apps directories then it builds an httpresponse based on the template. 

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])

		return redirect('/')

	
	# notað til að skila lista objectum og til að gera lúppu í html sjá home.html
	items = Item.objects.all()
			# Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
	return render(request, 'home.html', {'items': items})
	# return HttpResponse('<html><title>To-Do lists</title></html>')
