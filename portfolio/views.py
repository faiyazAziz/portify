from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Project, Education, Experience, Skill, Template
from django.core.mail import EmailMessage
import random
from .firebase import storage  # Import Firebase storage
from uuid import uuid4
base_temp_url_start = "https://firebasestorage.googleapis.com/v0/b/fir-63517.appspot.com/o/uploads%2F"
base_temp_url_end = ".png?alt=media&token=5523cb42-0762-48dc-bc08-dbb3b3c1f0a7"

tempaltes = [
            {'name':'one','title':'one','url':base_temp_url_start+'one.png'+base_temp_url_end},
            {'name':'two','title':'two','url':base_temp_url_start+'two.png'+base_temp_url_end},
        ]

def upload_to_firebase(file):
    filename = f"{uuid4()}_{file.name}"
    storage.child(f"uploads{filename}").put(file)
    return storage.child(f"uploads/{filename}").get_url(None)

# Create your views here.
def show(request,uuid):
    # print("inside show")
    temp = get_object_or_404(Template, uid=uuid)
    template_name = f"portfolio/{temp.name}.html"
    user = temp.user
    educations = Education.objects.filter(user=user)
    # print(educations)
    skills = Skill.objects.filter(user=user)
    projects = Project.objects.filter(user=user)
    return render(request,template_name,{'user':user,'educations':educations,'skills':skills,'projects':projects,'uid':uuid})

def form_show(request):
    if request.user.is_authenticated:
        print('authenticated')
        user = request.user
        educations = Education.objects.filter(user=user)
        skills = Skill.objects.filter(user=user)
        projects = Project.objects.filter(user=user)
        experiences = Experience.objects.filter(user=user)
        return render(request,'portfolio/portfolio_form.html',{'educations':educations,'skills':skills,'projects':projects,'templates':tempaltes})
    return redirect('register')

def portfolio_view(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('portfolio_name')
        email = request.POST.get('portfolio_email')
        number = request.POST.get('portfolio_number')
        role = request.POST.get('portfolio_role')
        about_me = request.POST.get('portfolio_about_me')
        gender = request.POST.get('portfolio_gender')
        dob = request.POST.get('portfolio_dob')
        profile_pic = request.FILES.get('portfolio_profile_pic')

        profile_pic_url = upload_to_firebase(profile_pic) if profile_pic else ''

        Portfolio.objects.create(
            user=user, name=name, email=email, number=number, role=role,
            gender=gender, about_me=about_me, dob=dob, profile_pic=profile_pic_url
        )
        return redirect('portfolio_form')

    return render(request, 'portfolio/portfolio_form.html')

def project_view(request):
    if request.method == 'POST':
        user = request.user
        project_title = request.POST.get('project_title')
        project_description = request.POST.get('project_description')
        project_url = request.POST.get('project_url')
        project_image = request.FILES.get('project_image')

        project_image_url = upload_to_firebase(project_image) if project_image else ''

        Project.objects.create(
            user=user, project_title=project_title, project_description=project_description,
            project_url=project_url, project_image=project_image_url
        )
        return redirect('portfolio_form')

    return render(request, 'portfolio/portfolio_form.html')
def education_view(request):
    if request.method == 'POST':
        user = request.user
        start_date = request.POST.get('education_start_date')
        passing_date = request.POST.get('education_passing_date')
        college_name = request.POST.get('education_college_name')
        course_name = request.POST.get('education_course_name')
        
        Education.objects.create(user=user, start_date=start_date, passing_date=passing_date, college_name=college_name, course_name=course_name)
        return redirect('portfolio_form')
    
    return render(request, 'portfolio/portfolio_form.html')

def experience_view(request):
    if request.method == 'POST':
        user = request.user
        start_date = request.POST.get('experience_start_date')
        end_date = request.POST.get('experience_end_date')
        job_title = request.POST.get('experience_job_title')
        company_name = request.POST.get('experience_company_name')
        description = request.POST.get('experience_description')
        
        Experience.objects.create(user=user, start_date=start_date, end_date=end_date, job_title=job_title, company_name=company_name, description=description)
        return redirect('portfolio_form')
    
    return render(request, 'portfolio/portfolio_form.html')

def skill_view(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('skill_name')
        score = request.POST.get('skill_score')
        
        Skill.objects.create(user=user, name=name, score=score)
        return redirect('portfolio_form')
    
    return render(request, 'portfolio/portfolio_form.html')

def handle_mail(request,uid):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email = EmailMessage(
            subject=f'message from {name}',
            body=message,
            from_email='theloonyguy@gmail.com',
            to = [user.email],
            reply_to=[user.email]
        )
        email.send()
    return redirect('user_website',uid)
 
 
def save_template(request,template):
    # if request.method == 'GET':
    # template = request.GET.get('template')
    print(template)
    print("template")
    user = request.user
    print(str(int(random.random()*1000)))
    cond = user.username + template + str(int(random.random()*1000))
    screenshot = base_temp_url_start + template + base_temp_url_end
    Template.objects.create(user=user,name=template,cond=cond,screenshot=screenshot)
    return redirect('dashboard',user.username)