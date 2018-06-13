from django.shortcuts import render,get_object_or_404
from .models import Logo
# Create your views here.

def home_view(request):
    return render(request , 'logos/home_page.html' ,{})
    
def logos_view(request):
    all_logos = Logo.objects.all()
    return render(request , 'logos/logos_page.html' , {'all_logos':all_logos})

def logo_detail_view(request,pk):
    logo = get_object_or_404(Logo,pk=pk)
    return render(request,'logos/logo_detail_page.html' ,{'logo':logo})
