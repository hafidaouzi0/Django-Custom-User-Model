from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin 
from .models import UserProfile

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model= UserProfile
    can_delete=False

class AccountsUserAdmin(UserAdmin):
    def add_view(self,*args,**kwargs) :
        self.inlines=[]
        return super(AccountsUserAdmin,self).add_view(*args,**kwargs)
    def change_view(self,*args,**kwargs ) :
        self.inlines=[UserProfileInline]
        return super(AccountsUserAdmin,self).change_view(*args,**kwargs)


admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)
