from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_1.models import Item, List

# Render function is a django function that takes a request as its first paramenter and 
# the name of the template to render as its second parameter. Django will automatically 
# search folders called templates in my apps directories then it builds an httpresponse based on the template. 

def home_page(request):
	
	return render(request, 'home.html')
	# return HttpResponse('<html><title>To-Do lists</title></html>')


def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
