from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        email_input = request.POST['email-input']
        return render(request, 'home.html', {'email_input': email_input})
        
    else:
        return render(request, 'home.html', {})

def impressum(request):
    return render(request, 'impressum.html', {})
