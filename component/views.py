from django.shortcuts import render,redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Registration,techblogs, verifiedEmail, InternshipModel, CompetetionModel, scholarshipModel, jobModel
from .utils import generate_otp, sendingmail
from .models import OTP
from .forms import hackathonRegForm, internshupUpdateForm, contactForm,competetionUpdateForm,scholarshipUpdateForm, jobUpdateForm


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
def login(request):
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
            return redirect('login')
        
    else:
        return render(request,'index.html')
    

# importing from otp project


# sendingmail(subject, message, recipient_list)
def emailotp(request):
    if request.method == 'POST':
        useremail = request.POST['email']
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

@login_required
def internshipupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = internshupUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'component/internshipupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'component/internshipupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = internshupUpdateForm()
    return render(request,'component/internshipupdates.html',{'forms':form})
    



@login_required
def competetionupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = competetionUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'component/competetionupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'component/competetionupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = competetionUpdateForm()
    return render(request,'component/competetionupdates.html',{'forms':form})
    





@login_required
def scholarshipupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = scholarshipUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'component/scholarshipupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'component/scholarshipupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = scholarshipUpdateForm()
    return render(request,'component/scholarshipupdates.html',{'forms':form})
    



@login_required
def jobupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = jobUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'component/jobupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'component/jobupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = jobUpdateForm()
    return render(request,'component/jobupdates.html',{'forms':form})
    




def opportunities(request):
    internships = InternshipModel.objects.all()
    competetion = CompetetionModel.objects.all()
    scholarship = scholarshipModel.objects.all()
    job = jobModel.objects.all()
    return render(request,'opportunities.html',
                  {'internships':internships,
                   'competetions':competetion,
                   'scholarships':scholarship,
                   'jobs':job
                   }
                  )

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



def courses(request):
    return render(request,'courses.html')


def linux(request):
    return render(request,'linux.html')

def python(request):
    return render(request,'python-course.html')

def C(request):
    return render(request,'C.html')

def HTML(request):
    return render(request,'HTML.html')

def css(request):
    return render(request,'css.html')


def book(request):
    return render(request,'book.html')


def about(request):
    return render(request,'about.html')


def copyright(request):
    return render(request,'copyright.html')


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('msg') 
    else:
        form = contactForm()
    return render(request,'contact.html',{'forms':form})



# @login_required
def profile_page(request):
    user = request.user
    return render(request, 'profile_page.html')

def notespedia(request):
    opportunities_for_fresher= ['Web Developer', 'App Developer' , 'Software Engineer', 'iOS Engineer', 'AI Developer', 'NLP Engineer', 'Data Scientist','Data Analyst', 'Data Engineer', 'Course Engineer']
    referance_books=['Sebesta, "Concept of Programming Language", Addison Wesley, 4th Edition, 2019',
                     ' Deitel & Deitel, “Internet and World Wide Web – How to Program”, Goldberg,Pearson Education. 3rd Edition 2003',
                     'Petersons, "Operating Systems", Addison Wesley, 9th Edition, 2012',
                     'Forouzan, B. A., Data Communications and Networking, McGraw-Hill Higher Education,3rd Edition, 2004.',
                     'A.S. Tannenbaum, “Computer Networks”, 3rd Edition, Prentice Hall India, 1997.']
    context= {
        'opportunities_for_fresher':opportunities_for_fresher,
        'referance_books':referance_books
    }
    return render(request,'notespedia.html',context)



def cse(request):
    return render(request,'cse.html')



def et(request):
    return render(request,'et.html')


def loginerror(request):
    return render(request,'loginerror.html')

def team(request):
    return render(request,'team.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')


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






# connection = psycopg2.connect(**db_config)
# cursor = connection.cursor()
# query = "select rank from \"profile\";"
# cursor.execute(query)

# sql_query = "SELECT * FROM \"user\" where username = 'edith27401';"
# cursor.execute(sql_query)

# rows = cursor.fetchall()
# res = rows
# print(res[0][0])


# random

def logout_view(request):
    logout(request)
    return redirect("home")

    
# def profile_page(request):
#     return render(request,'profile_page.html')
    