from django.shortcuts import render
from .models import BlogModel
from django.core.paginator import Paginator,PageNotAnInteger
# Create your views here.
def home(request):
	return render(request, 'home.html')

def home_Programing(request,tipe):
	if tipe == "C":
		data=BlogModel.objects.filter(category="P",sub_category="C")
		data1=BlogModel.objects.filter(category="P",sub_category="C",id=1)
		ttl = ["C PROGRAMING TUTORIAL"]
		print(data)

		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl })
	elif tipe == "CPP":
		data=BlogModel.objects.filter(category="P",sub_category="CPP")
		data1=BlogModel.objects.filter(category="P",sub_category="CPP",id=1)
		ttl = ["C++ PROGRAMING TUTORIAL"]
		print(data1)
		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "JV":
		data=BlogModel.objects.filter(category="P",sub_category="JV")
		data1=BlogModel.objects.filter(category="P",sub_category="JV",id=1)
		ttl = ["JAVA PROGRAMING TUTORIAL"]
		print(data1)
		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "PY":
		data=BlogModel.objects.filter(category="P",sub_category="PY")
		data1=BlogModel.objects.filter(category="P",sub_category="PY",id=1)
		ttl = ["PYTHON PROGRAMING TUTORIAL"]
		print(data1)
		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "FL":
		data=BlogModel.objects.filter(category="P",sub_category="FL")
		data1=BlogModel.objects.filter(category="P",sub_category="FL",id=1)
		ttl = ["FLUTTER PROGRAMING TUTORIAL"]
		print(data1)
		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl})
	else:
		return render(request, 'soon.html')

def home_Project(request, tipe):
	if tipe == "C":
		data=BlogModel.objects.filter(category="PR",sub_category="C")
		data1=BlogModel.objects.filter(category="PR",sub_category="C",id=1)
		ttl = ["C PROGRAMING PROJECT"]
		pagig = Paginator(data,per_page=2)
		page_number = request.GET.get('page')
		page_object = pagig.get_page(page_number)
		print(pagig.object_list)
		return render(request, 'blog/project/home.html',{'data':page_object})
	elif tipe == "CPP":
		data=BlogModel.objects.filter(category="PR",sub_category="CPP")
		data1=BlogModel.objects.filter(category="PR",sub_category="CPP",id=1)
		ttl = ["C++ PROGRAMING PROJECT"]
		print(data1)
		return render(request, 'blog/project/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "JV":
		data=BlogModel.objects.filter(category="PR",sub_category="JV")
		data1=BlogModel.objects.filter(category="PR",sub_category="JV",id=1)
		ttl = ["JAVA PROGRAMING PROJECT"]
		print(data1)
		return render(request, 'blog/project/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "PY":
		data=BlogModel.objects.filter(category="PR",sub_category="PY")
		data1=BlogModel.objects.filter(category="PR",sub_category="PY",id=1)
		ttl = ["PYTHON PROGRAMING PROJECT"]
		print(data1)
		return render(request, 'blog/project/home.html',{'data':data,'data1':data1,'ttl':ttl})
	elif tipe == "FL":
		data=BlogModel.objects.filter(category="PR",sub_category="FL")
		data1=BlogModel.objects.filter(category="PR",sub_category="FL",id=1)
		ttl = ["FLUTTER PROGRAMING PROJECT"]
		print(data1)
		return render(request, 'blog/project/home.html',{'data':data,'data1':data1,'ttl':ttl})
	else:
		return render(request, 'soon.html')


def detail_Programing(request,tipe,slug):
	if tipe == "C":
		data=BlogModel.objects.filter(category="P",sub_category="C")
		data1=BlogModel.objects.filter(category="P",sub_category="C",slug=slug)
		ttl = ["C PROGRAMING TUTORIAL"]
		print(data)
		return render(request, 'blog/programing/home.html',{'data':data,'data1':data1,'ttl':ttl })
	else:
		return render(request, 'soon.html')

def detail_Project(request,tipe,slug):
	if tipe == "C":
		data=BlogModel.objects.filter(category="PR",sub_category="C")
		data1=BlogModel.objects.filter(category="PR",sub_category="C",slug=slug)
		ttl = ["C PROGRAMING TUTORIAL"]
		print(data)
		return render(request, 'blog/project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
	else:
		return render(request, 'soon.html')