from django.shortcuts import render
from .models import Users

# Create your views here.

def SignupPage(requst):
    return render(requst, 'SignupPage.html')

def UsersPage(requst):
   ID = requst.post.get("ID")
   FN = requst.post.get("FirstName")
   LN = requst.post.get("LastName")
   Email = requst.post.get("Email")
   Pass = requst.post.get("PassWord")

   o_ref = Users(ID=ID, FirstName=FN, LastName=LN, Email=Email, PassWord=Pass)
   o_ref.save()

   return render(requst,'PopUps.html')
