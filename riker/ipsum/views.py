from rikeripsum import rikeripsum
from django.shortcuts import render
from django.http import *



# Create your views here.
def create_index(request):
	ipsum = rikeripsum.generate_paragraph()
	if request.is_ajax():
		return HttpResponse(ipsum)
	context = {"ipsum" : ipsum}
	return render(request, "index.html", context)

def create_ipsum(request):
	ipsum = rikeripsum.generate_paragraph()
	if request.is_ajax():
		return HttpResponse(ipsum)
	return HttpResponse(ipsum)
