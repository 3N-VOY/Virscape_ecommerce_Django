from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import SignUpForm, EditUserForm
from .models import Profile, User
from django.contrib.auth.decorators import login_required
from shop.models import Item
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user instance but don't save yet
            user.username = user.email  # Set username to the same as the email
            user.save()  # Now save the user instance
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.profile.location = form.cleaned_data.get('location')
            
            
            user.profile.first_name = form.cleaned_data['first_name']
            user.profile.last_name = form.cleaned_data['last_name']
            user.profile.country = form.cleaned_data['country']
            user.profile.address = form.cleaned_data['address']
            user.profile.zipcode = form.cleaned_data['zipcode']
            user.profile.city = form.cleaned_data['city']
            
            
            user.profile.save()  # Save the profile instance
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'userprofiles/register.html', {'form': form})



def loginpage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            print("error email or password")

    context = {}
    return render(request, 'userprofiles/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('homepage')


def myaccount(request, pk):
    user = get_object_or_404(User, id=pk)
    context = {'user':user}
    return render(request, "userprofiles/account_page.html", context)

@login_required
def add_favourites(request, id):
    item = get_object_or_404(Item, id=id)
    if item.favourites.filter(id=request.user.id).exists():
        item.favourites.remove(request.user)
    else:
        item.favourites.add(request.user)
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        
@login_required
def favourites_list(request):
    item = Item.objects.filter(favourites=request.user).order_by('-created_date')
    context = {'item':item}
    return render(request, 'userprofiles/favourites.html', context)

@login_required
def edit_profile(request, id):
    user = get_object_or_404(User, id=id)
    
    
    
    if request.method == 'GET':
        context = {'form': EditUserForm(instance=request.user.profile), 'id':id}
        return render(request,  'userprofiles/edit_account.html', context)
    
    elif request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Credentials Saved.')
            return redirect('homepage')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'userprofiles/edit_account.html',{'form':form})
    