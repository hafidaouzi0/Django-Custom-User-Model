from django.shortcuts import render,redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileForm
# Create your views here.


@login_required
#this one will make sure that forms are both saved in the database 
#if there's a problem with any of the forms  none of them won't be saved
@transaction.atomic
def update_profile(request):
    #request.POST to save the data the user has enterd in the forms
    user_form=UserForm(request.POST,instance=request.user)
    user_profile_form=UserProfileForm(request.POST,instance=request.user.userprofile)
    if request.method == 'POST':
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
        return redirect('/profile')
    else:
        user_form=UserForm(instance=request.user)
        user_profile_form=UserProfileForm(instance=request.user.userprofile)
    return render(request,"profile.html",{"u_form":user_form,"p_form":user_profile_form})
