from django.shortcuts import render

# Create your views here. 
# A view is a place where we put the "logic" of our application.
# Views are just Python functions that are a little bit more complicated 

def post_list(request):
	return render(request, 'blog/post_list.html', {})

