from django.shortcuts import render
import json

# Create your views here.

import requests

url = "xyz"

headers = {
    'x-rapidapi-key': "xyz",
    'x-rapidapi-host': "01234"
    }

response = requests.request("GET", url, headers=headers).json

# print(response.text)
def helloworld(request):
	mylist=[]
	noofresults=int(response['results'])

	for x in range(0,noofresults):

		mylist.append(response['response'][x]['country'])

	if request.method=="POST":
		selectedcountry=request.POST['selectedcountry']
		
		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country']:
				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)

		context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
		return render(request,'helloworld.html',context)
				
	context={'mylist':mylist}
	return render(request,'helloworld.html',context)