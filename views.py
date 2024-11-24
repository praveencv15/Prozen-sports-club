from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Sports_details, Store, Member_details, TournamentRegistration
from .forms import NewItemForm, NewStoreForm, TournamentRegistrationForm
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    return render(request, 'core/login.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('core:index')
    return redirect('core:login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:index')  
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

def index(request):
    sports = Sports_details.objects.all() 
    tournaments = TournamentRegistration.objects.all()
    return render(request, 'core/index.html', {'sports': sports, 'tournaments': tournaments})

def tournament_detail(request, pk):
    tournament = get_object_or_404(TournamentRegistration, pk=pk)

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        
        send_mail(
            subject="Tournament Registration Successful",
            message=f"Dear {name},\n\nThank you for registering for the tournament. We look forward to seeing you!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        success_message = f"Thank you for registering, {name}!"
        return render(request, "core/tournament_detail.html", {"tournament": tournament, "success_message": success_message})

    return render(request, "core/tournament_detail.html", {"tournament": tournament})

def sport_tournaments(request, sport_name):
    tournaments = TournamentRegistration.objects.filter(sport=sport_name)
    context = {
        "sport_name": sport_name,
        "tournaments": tournaments,
    }
    return render(request, "core/filterindex.html", context)

@login_required
def storage(request):
    items = Store.objects.all()
    return render(request, 'core/store.html', {'items': items})

@login_required
def member(request):
    details = Member_details.objects.all()
    return render(request, 'core/members.html', {'details': details})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New member has been added successfully!") 
            return redirect("core:storage") 
        else:
            print(form.errors)
    else:
        form = NewItemForm()
    return render(request, 'core/more.html', {
        'form': form,
        'title': 'New Member',  
    })

@login_required
def det(request):
    if request.method == 'POST':
        form = NewStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New store item has been added successfully!")
            return redirect("core:storage")  # Redirecting after successful store item creation
    else:
        form = NewStoreForm()
    return render(request, 'core/new.html',{
        'form': form,
        'title': 'New Item',
        })

def logout(request):
    django_logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('sessionid')
    return response

def admin(request):
    sports = Sports_details.objects.all().count()
    details = Member_details.objects.all().count()
    items = Store.objects.all().count()
    con = {'mem': details, 'spo': sports, 'item': items}
    return render(request, 'core/admin.html', {'con': con})

def member_detail(request, member_id):
    member = get_object_or_404(Member_details, id=member_id)
    return render(request, 'core/memberView.html', {'member': member})

def tournament_registration(request):
    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()

            # Send confirmation email
            user_email = form.cleaned_data['email']
            send_mail(
                subject="Tournament Registration Successful",
                message=f"Dear {registration.name},\n\nThank you for registering for the tournament in {registration.sport}. We look forward to seeing you!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
            )
            return redirect('core:tournament_registration_success')
    else:
        form = TournamentRegistrationForm()
    return render(request, 'core/tournament_registration.html', {'form': form})

def tournament_registration_success(request):
    return render(request, 'core/tournament_registration_success.html')

def tournament_registration_view(request):
    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()

            user_email = form.cleaned_data.get('email')
            subject = "Tournament Registration Successful"
            message = f"Dear {registration.name},\n\nThank you for registering for the tournament in {registration.sport}. We look forward to seeing you!"
            from_email = settings.DEFAULT_FROM_EMAIL  # Use settings for email
            recipient_list = [user_email]

            # Send the confirmation email
            send_mail(subject, message, from_email, recipient_list)

            return redirect('core:registration_success')  
    else:
        form = TournamentRegistrationForm()

    return render(request, 'core/tournament_registration.html', {'form': form})

def registration_success_view(request):
    return render(request, 'core/registration_success.html')  
