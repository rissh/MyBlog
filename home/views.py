from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import PasswordInput
from django.shortcuts import redirect, render, HttpResponse
from blog.models import Post
from home.models import Contact
# Create your views here.
def  home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("THIS IS THE HOME PAGE")

def  about(request):
    return render(request, 'home/about.html')

    # return HttpResponse("THIS IS THE ABOUT PAGE")


def  contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request,"Please fill the form properly")
        else:
            contact  = Contact(name=name, email=email, phone=phone, content = content)
            contact.save()
            messages.success(request, "Your response has been submitted sucessfully")
    return render(request, 'home/contact.html')

# return HttpResponse("THIS IS THE CONTACT PAGE")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPosts= Post.objects.filter(title__icontains=query)
        allPosts= Post.objects.filter(author__icontains=query)
        allPosts= Post.objects.filter(content__icontains=query)

    if allPosts.count()==0:
        messages.warning(request,"No search results found. Please refine your query")
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)

def blogSignup(request):
    if request.method == 'POST':

        username=request.POST['username']
        inputfname = request.POST['inputfname']
        inputlname = request.POST['inputlname']
        inputemail = request.POST['inputemail']
        inputPass1 = request.POST['inputPass1']
        inputPass2 = request.POST['inputPass2']


        

        # check for errorneous input
        

        
        if (inputPass1 != inputPass2):
            messages.error(request,"Passwords do not match, Please check the password and try again")
            return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, inputemail, inputPass1)
        myuser.first_name= inputfname
        myuser.last_name= inputlname
        myuser.save()
        messages.success(request, "Your Blog account has been created")
        return redirect('home')

    else:
        return HttpResponse('Page Not Found')

def blogLogin(request):
    if request.method == "POST":
        # parameter for the post
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']


        user=authenticate(username=loginusername, password=loginpassword)
        if user is None:
            messages.error(request, "Invalid credentials, Please check and retry")
            return redirect('home')

        else: 
            login(request, user)
            messages.success(request, "Yayy !! You are successfully Logged In")
            return redirect('home')
    return HttpResponse("Error 404 - Not Found")

def blogLogout(request):
    logout(request)
    messages.success(request, "Succesfully Logged Out")
    return redirect('home')