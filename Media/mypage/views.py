from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, FileResponse, Http404


def home(request):
  image_url = settings.STATIC_URL
  video_url = settings.MEDIA_URL
  context = {
      "images": [
          {"ocean": image_url + "images/ocean.jpg"},
          {"nature": image_url + "images/nature.jpg"},
          {"cartoon": video_url + "media/document"},
      ],
  }
  return render(request, 'index.html', context)


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)  
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
    else:
        raise Http404("File not found")

from django.template.loader import get_template

def debug_template_path(request):
    try:
        get_template('index.html')
        return HttpResponse("Template found!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    