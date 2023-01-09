from django.db import models
from django.contrib.auth.models import User

#if you wanna add your own behaviors and managers while extending the user model we use custom manager
class PersonManagerInactive(models.Manager):

     def get_queryset(self):
         return super(PersonManagerInactive,self).get_queryset().filter(is_active=False)

class PersonManagerActive(models.Manager):

     def get_queryset(self):
         return super(PersonManagerActive,self).get_queryset().filter(is_active=True)



#a proxy model makes you inhiret from the user model without creating its own table in database
#and it prevents you from adding or removing fields or behaviors
class Person(User):
    inactive=PersonManagerInactive()
    active=PersonManagerActive()

    class Meta:
        proxy=True
        ordering=['first_name']

#this method used to count all the inactive users
    @classmethod
    def count_all(cls):
        return cls.objects.filter(is_active=True).count()

    def check_active(self):
        if self.is_active == True:
             return "you are active"
        else:
             return "you are not active"

    def __str__(self):
        return self.first_name

#Person.inactive.all()  : for inactive users
#Person.active.all()    : for active users