from rikeripsum import rikeripsum
from django.shortcuts import render
from django.http import *



# Create your views here.
def create_ipsum(request):
	ipsum = rikeripsum.generate_paragraph()
	context = {"ipsum" : ipsum}
	return render(request, "index.html", context)
