from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserForm, UserForm
# Create your views here.
# Libraries for django Login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
     return HttpResponse('You are logged in')

def index(request):
    return render(request,'app_password_auth/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        fu = UserForm(data = request.POST)
        fcu = CustomUserForm(data = request.POST)


        if fu.is_valid() and fcu.is_valid():
            user = fu.save()
            user.set_password(user.password)
            user.save()

            profile = fcu.save(commit=False)

            """
            profile is an instance of fcu.
            fcu is an instance of CustomUserForm.
            CustomUserForm is configured to the model of EndUserProfileInfo.
            EndUserProfileInfo class has end_user = models.OneToOneField(User, on_delete = models.CASCADE)
            """
            profile.user = user

            if 'end_user_dp' in request.FILES:

                """
                request.FILES is USED FOR ALL UPLOADED FILES LIKE .CSV .TXT .JPEG .PNG etc.
                """
                profile.end_user_dp = request.FILES['end_user_dp']

            profile.save()
            registered = True
        else:
            print(fu.errors, fcu.errors)
    else:
        fu = UserForm()
        fcu = CustomUserForm()

    return render(request, 'app_password_auth/registration_page.html', {'user_form':fu, 'user_profile_form':fcu, 'registered':registered})

# Do not use class name as login as we already have imported login form django.contrib.auth
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')

        # the django function will authenticate the user
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                # use the login function which you have imported from django
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not activated")
        else:
            print("The username {} with password {} tried to login".format(username, password))
            return HttpResponse("User authentication failed")
    else:
        return render(request, 'app_password_auth/user_login.html', {})
