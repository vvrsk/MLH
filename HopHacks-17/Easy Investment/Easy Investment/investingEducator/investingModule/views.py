# Create your views here.
import functions
from django.shortcuts import render, HttpResponse
from django.template import loader
import json
import urllib

def index(request):
    return HttpResponse('Hello World!')

	
def userDetails(request):
	request.session["chosenValue"] = request.POST.get("link")
	print(request.session["chosenValue"])
	if request.method == 'POST' and request.session["chosenValue"] is not None:		
		return HttpResponse(stockDetails(request))		
	listOfCategoryPages = []
	listOfLikedPagesMain = []
	listOfLikedPages={'name':[]}
	temp = []
	data = []
	template = loader.get_template(r'<FilePath>\profile.html')
	data_file = getFBResults(<tokenValue>)
	data = json.load(data_file)	
	return HttpResponse(template.render({'listOfLikedPagesMain': data},request))

	
def landingPage(request):
	template = loader.get_template(r'<FilePath>\landingPage.html')
	return HttpResponse(template.render({},request))
	
	
def stockDetails(request):
	template = loader.get_template(r'<FilePath>\Final Page.html')
	return HttpResponse(template.render({},request))