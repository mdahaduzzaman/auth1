from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

CustomUser = get_user_model()  # Get the custom user model

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['repeat_password']

        if password1 == password2:
            # Create a new user object
            user = CustomUser.objects.create_user(username=username, email=email, password=password1)
            
            # You can optionally log the user in after registration
            # using Django's built-in login function.
            # For example: login(request, user)
            
            return redirect('registration_success')  # Redirect to a success page
        else:
            error_message = "Passwords do not match."
            return render(request, 'security/signup.html', {'error_message': error_message})
    else:
        return render(request, 'security/signup.html')


















def index(request):
    return render(request, 'security/index.html')

def signin(request):
    return render(request, 'security/signin.html')

def reset_password(request):
    return render(request, 'security/reset_password.html')




