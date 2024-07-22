from django.shortcuts import render,redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Registration,techblogs, verifiedEmail, UserActivity
from .utils import generate_otp, sendingmail
from .models import OTP
from .forms import hackathonRegForm


import psycopg2

# PostgreSQL connection parameters
# db_config = {
#     'dbname': 'postgres',
#     'user': 'fx818',
#     'password': '@Anurag818@',
#     'host': 'learnwithus.postgres.database.azure.com',
#     'port': '5432'
# }

# db_config = psycopg2.connect(user="fx818", password="@Anurag818@", host="learnwithus.postgres.database.azure.com", port=5432, database="postgres")


# db_config = {
#     'user': 'postgres.mvaonazvlarpgxcrjpsp',
#     'password': '@learnwithus818@',
#     'host': 'aws-0-ap-south-1.pooler.supabase.com',
#     'port': 5432,
#     'database': 'postgres'
# }
# connection = psycopg2.connect(**db_config)






def logout(request):
    auth.logout(request)
    return redirect('home')


# Login
def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(
            username = username,
            password = password
        )

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('userlogin')
        
    else:
        return render(request,'index.html')
    

# importing from otp project


# sendingmail(subject, message, recipient_list)
def emailotp(request):
    if request.method == 'POST':
        useremail = request.POST['email']
        
        if verifiedEmail.objects.filter(email=useremail).exists():
            messages.info(request,"Email already exists. Please use another email")
            return render(request,'component/emailotp.html')

        otp = generate_otp()
        # Save OTP to the database
        OTP.objects.create(useremail=useremail, otp=otp)

        # Leaving it some work is still left like if email already exist then what to do??

        addEmail = verifiedEmail.objects.create(email = useremail, isVerified = False)
        addEmail.save()


        # Sending OTP
        subject = 'OTP verfiication'
        message = f"Your One Time Password is : {otp}"
        reciever = [useremail]
        sendingmail(subject, message, reciever)
        print("\nMail sent successfully\n")
        
        request.session['useremail'] = useremail
        return redirect('verifyotp')
    
    return render(request, 'component/emailotp.html')


def verifyotp(request):
    if request.method == 'POST':
            otp_input = request.POST['otp_input']
            useremail = request.session.get('useremail')
            
            try:
                otp_record = OTP.objects.get(useremail=useremail, otp=otp_input)
                if otp_record.is_valid():
                    addEmail = verifiedEmail.objects.get(email = useremail)
                    addEmail.isVerified = True
                    addEmail.save()
                    return render(request, 'component/finalregister.html')
                else:
                    return render(request, 'component/verifyotp.html')
            except OTP.DoesNotExist:
                messages.info(request, "Some error occured with the OTP.")
                return render(request, 'component/verifyotp.html')
    
    return render(request, 'component/verifyotp.html')

def finalregister(request):
    useremail = request.session.get('useremail')
    print("User email from session is: ",useremail)
    try:
        Verified = verifiedEmail.objects.get(email=useremail).isVerified
    except:
        Verified = False
    if Verified == False:
        messages.info(request,"Email not verified till now")
        return render(request,'component/emailotp.html')
    if request.method == "POST":
        name = request.POST['fullname']
        username = request.POST['username']
        email = useremail
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        gender = request.POST['gender']
        profile_pic = request.FILES.get('profile_pic')

        skills = request.POST['skills']
        country = request.POST['country']
        linkedin = request.POST['linkedin']
        activitypoint = 0

        if password1 != password2:
            messages.info(request,'Sorry, Your password doesnot match!')
            return render(request,'component/finalregister.html')

        skill1 = skills.split(',')[0]
        skill2 = skills.split(',')[1]
        skill3 = skills.split(',')[2]

        User = get_user_model()

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'component/finalregister.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'component/finalregister.html')

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            skill1=skill1,
            skill2=skill2,
            skill3=skill3,
            country=country,
            linkedin=linkedin,
            activitypoint=activitypoint, 
            profile_pic=profile_pic
        )
        user.save()
        user = auth.authenticate(
            username = username,
            password = password1
        )
        auth.login(request,user)

        # Redirecting to the Homepage
        return redirect('home')

    return render(request,'component/finalregister.html')

@login_required
def edit_your_profile(request):
    User = get_user_model()
    user = request.user
    if request.method == 'POST':    
        name = request.POST['fullname']
        newusername = request.POST['username']
        newfirst_name = name.split(' ')[0]
        newlast_name = name.split(' ')[1]
        newgender = request.POST['gender']
        newprofile_pic = request.FILES.get('profile_pic')

        # newskills = request.POST['skills']
        newcountry = request.POST['country']
        newlinkedin = request.POST['linkedin']
        newactivitypoint = 0

        try:
            image = request.FILES['profile_pic']
        except:
            image = user.profile_pic
        
        newskill1 = request.POST['skill1']
        newskill2 = request.POST['skill2']
        newskill3 = request.POST['skill3']

        if newusername != user.username:
            if User.objects.filter(username=newusername).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'component/edit_your_profile.html')
        
        
        newUser = User.objects.filter(username = user.username)
        try:
            for i in newUser:
                i.username = newusername
                i.first_name = newfirst_name
                i.last_name = newlast_name
                i.gender = newgender
                i.profile_pic = newprofile_pic
                i.country = newcountry
                i.skill1=newskill1
                i.skill2=newskill2
                i.skill3=newskill3
                i.linkedin = newlinkedin
                i.profile_pic = image
                i.save()
                print("Updated the user data")
        except:
            print("Pakka idhar hi error hai bhai")
        return redirect('profile_page')
    # print(user.username)
    return render(request,'component/edit_your_profile.html')



# Modifying the User and making CustomUser
# def register(request):
#     if request.method == 'POST':

#         name = request.POST['name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = name.split(' ')[0]
#         last_name = name.split(' ')[1]
#         gender = request.POST['gender']
#         profile_pic = request.FILES.get('profile_pic')

#         skills = request.POST['skills']
#         country = request.POST['country']
#         linkedin = request.POST['linkedin']
#         activitypoint = 0

#         if password1 != password2:
#             messages.info(request,'Sorry, Your password doesnot match!')
#             return render(request,'register.html')

#         skill1 = skills.split(',')[0]
#         skill2 = skills.split(',')[1]
#         skill3 = skills.split(',')[2]

#         User = get_user_model()

#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists.')
#             return render(request, 'register.html')

#         # Check if the email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists.')
#             return render(request, 'register.html')


#         # before creating a user we would like to verify the user email via otp





#         # Create the user
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1,
#             first_name=first_name,
#             last_name=last_name,
#             gender=gender,
#             skill1=skill1,
#             skill2=skill2,
#             skill3=skill3,
#             country=country,
#             linkedin=linkedin,
#             activitypoint=activitypoint, 
#             profile_pic=profile_pic
#         )
#         user.save()
#         user = auth.authenticate(
#             username = username,
#             password = password1
#         )
#         auth.login(request,user)

#         # Redirecting to the Homepage
#         return redirect('home')

#     return render(request, 'register.html')


def home(request):
    return render(request,'home.html')

# @login_required
def techblog(request):
    user = request.user
    if user.id is not None:
        all_blogs = techblogs.objects.all()
        id = user.id
        blogs_by_user = techblogs.objects.filter(username = id)
        blogs_by_user = blogs_by_user[::-1]
        
        return render(request,'techblog.html',{
            'blogs':blogs_by_user
        })
    else:
        blogs_by_user = techblogs.objects.all()
        blogs_by_user = blogs_by_user[::-1]
        
        return render(request,'techblog.html',{
            'blogs':blogs_by_user
        })


def hackathon(request):
    if request.method == 'POST':
        form = hackathonRegForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'msg.html')
        else:
            return render(request,'hackathon.html',{'forms':form})

    else:
        form = hackathonRegForm()
    return render(request,'hackathon.html',{'forms':form})


def githubblog(request):
    return render(request,'allblogs/explore-github.html')

def msg(request):
    return render(request,'msg.html')


@login_required
def writetechblog(request):
    
    if request.method == "POST":
        title = request.POST['title']
        link = request.POST['link']
        description = request.POST['description']

        user = request.user
        
        add_blog = techblogs.objects.create(
            username = user,
            title = title,
            link = link,
            description = description
        )
        add_blog.save()
        messages.info(request,'Written Sucessfully')
        return redirect('techblog')
    
    else:
        return render(request,'writetechblog.html')



def book(request):
    return render(request,'book.html')





# @login_required
def profile_page(request):
    user = request.user
    activities = UserActivity.objects.filter(user=user.pk)
    activities = activities[::-1][:7]
    # print(activities)
    for activity in activities:
        print(activity.path)
    return render(request, 'profile_page.html',{'activities':activities})







def loginerror(request):
    return render(request,'loginerror.html')



def daily_leetcode_questions(request):

    daily_link = "<iframe height='400rem' width='750rem' src='https://www.youtube.com/embed/4DsZZ_otpU8?si=pO0aPdIMllp6ULM1' title='YouTube video player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' referrerpolicy='strict-origin-when-cross-origin' allowfullscreen></iframe>"
    
    daily = {
        'link' : daily_link
    }

    return render(request, 'daily_leetcode_questions.html',daily)


def soon(request):
    return render(request, 'soon.html')




def news(request):
    import requests
    api_key = 'a83ab2795c40404a822cb5e4fb524682'
    # url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a83ab2795c40404a822cb5e4fb524682'
    # url = 'https://newsapi.org/v2/top-headlines?category=technology&apiKey=a83ab2795c40404a822cb5e4fb524682'
    url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a83ab2795c40404a822cb5e4fb524682'
    data = requests.get(url)
    result = data.json()

    # print(result)
    # print(result['status'])
    # print(result['totalResults'])
    # print(result['articles'][0])
    # print(result['articles'][0]['source'])
    # print(result['articles'][0]['author'])
    # print('Article title : ',result['articles'][0]['title'])
    # print('Article description : ',result['articles'][0]['description'])

    data_to_send = {
        'allarticle': result['articles'],
        'total': result['totalResults']
    }

    return render(request,'news.html',data_to_send)


def logout_view(request):
    logout(request)
    return redirect("home")

