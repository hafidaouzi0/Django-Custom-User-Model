from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


#we can add additional fields to the User model
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField(null=True,blank=True)
    nickname=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username
    #the concept of receiver notify us whenever a user has been created 
    #so we can use it to add a new user_profile whenever a user has been created 
    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    


#To comment out multiple lines of code in Python in Windows, you can use the following steps:

# Select the lines of code that you want to comment out.
# Press "Ctrl + /" on your keyboard. This will add a "#" symbol at the beginning of each selected line, effectively commenting them out.

# #if you wanna add your own behaviors and managers while extending the user model we use custom manager
# class PersonManagerInactive(models.Manager):

#      def get_queryset(self):
#          return super(PersonManagerInactive,self).get_queryset().filter(is_active=False)

# class PersonManagerActive(models.Manager):

#      def get_queryset(self):
#          return super(PersonManagerActive,self).get_queryset().filter(is_active=True)



# #a proxy model makes you inhiret from the user model without creating its own table in database
# #and it prevents you from adding or removing fields or behaviors
# class Person(User):
#     inactive=PersonManagerInactive()
#     active=PersonManagerActive()

#     class Meta:
#         proxy=True
#         ordering=['first_name']

# #this method used to count all the inactive users
#     @classmethod
#     def count_all(cls):
#         return cls.objects.filter(is_active=True).count()

#     def check_active(self):
#         if self.is_active == True:
#              return "you are active"
#         else:
#              return "you are not active"

#     def __str__(self):
#         return self.first_name

#Person.inactive.all()  : for inactive users
#Person.active.all()    : for active users