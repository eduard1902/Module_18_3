from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home_view(request):
    return render(request, 'class_template.html')

class HomeView(TemplateView):
    template_name =('func_template.html')