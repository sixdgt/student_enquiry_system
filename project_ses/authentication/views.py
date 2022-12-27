from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")

class RegisterView(View):
    def get(self, request):
        return render(request, "authentication/register.html")
    
    def post(self, request):
        req_username = request.POST.get('username')
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        user = User.objects.create_user(username=req_username, email=req_email)
        user.password = req_password
        user.is_active = True
        user.save()
