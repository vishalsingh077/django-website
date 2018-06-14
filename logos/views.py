from django.shortcuts import render,get_object_or_404
from .models import Logo

# for downloading files
from django.http import FileResponse
from django.utils.text import slugify
import os

def home_view(request):
    return render(request , 'logos/home_page.html' ,{})
    
def logos_view(request):
    all_logos = Logo.objects.all()
    return render(request , 'logos/logos_page.html' , {'all_logos':all_logos})

def logo_detail_view(request,pk):
    logo = get_object_or_404(Logo,pk=pk)
    return render(request,'logos/logo_detail_page.html' ,{'logo':logo})

def search_view(request):
    query = request.GET.get('q')
    searched_logos = Logo.objects.filter(logo_name__contains = query)or Logo.objects.filter(logo_type__contains = query)
    context = {'searched_logos':searched_logos , 'query' : query}
    return render(request , 'logos/search_page.html' , context)


def logo_download_view(request, pk):
    item = get_object_or_404(Logo, pk=pk)
    file = item.logo_img
    file_name, file_extension = os.path.splitext(file.url)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(file, 
      content_type = "file/%s"  %(file_extension))
    response["Content-Disposition"] = "attachment;"\
        "filename=%s-%s.%s" %(item.logo_name,item.logo_type,file_extension)
    return response























