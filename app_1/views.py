from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_1.models import Item

# Render function is a django function that takes a request as its first paramenter and 
# the name of the template to render as its second parameter. Django will automatically 
# search folders called templates in my apps directories then it builds an httpresponse based on the template. 

def home_page(request):
	
	return render(request, 'home.html')
	# return HttpResponse('<html><title>To-Do lists</title></html>')


def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
