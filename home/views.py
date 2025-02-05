from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})

def register(request):
    template_data = {}
<<<<<<< HEAD
    template_data['title'] = 'Register/SSOO'
=======
    template_data['title'] = 'Register'
>>>>>>> 98378ca (Committing)
    return render(request, 'home/about.html', {'template_data': template_data})
