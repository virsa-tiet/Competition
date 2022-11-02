
from django.http import HttpResponse
from django.shortcuts import redirect , render
from .models import Participant
# from django.contrib import messages
import csv
# Create your views here.
import requests
sheetly_header={
    "Authorization": "Bearer gffgfgfggff"
    }
sheetly_endpoint="https://api.sheety.co/78eda28988cc9dbe69ca0a6bb25df255/work/sheets"


all_participants= Participant.objects.all
def home(request):
    return render(request , 'home.html' , {'all':all_participants})

def come(request):
    
    if request.method == "POST" :
        
        name = request.POST['name']
        branch = request.POST['branch']
        phone = request.POST['phone']
        roll = request.POST['roll']
        email = request.POST['email']
        subit = request.POST['subit']
        subit1 = request.POST['subit1']
        data=Participant.objects.create(
        name=name,
        branch=branch,
        email =email,
        roll= roll,
        phone=phone,
        subit=subit,
        subit1=subit1
        )
        data.save()
        with open('participants1.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    data1=[name,branch,email,roll,phone,subit,subit1]
                    spamwriter.writerow(data1) 



        sheetly_params = {
        "work": {
            "name":name,
            "branch":branch,
            "email":email,
            "roll":roll,
            "phone":phone,
            "subit":subit,
            "subit1":subit1
             
        }
        }
        
        response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
        return render(request,'thankyou.html')     
    return render(request , 'come.html')





















# data=Participant.objects.create(
        # name=name,
        # branch=branch,
        # email =email,
        # roll= roll,
        # phone=phone,
        # subit=subit
        # )
        # data.save()
        # form.save()



# context={ 'name':name,
        #      'branch':branch,
        #      'email' :email,
        #      'roll': roll,
        #       'phone':phone,
        #       'subit':subit
        #      }




  
        # if form.is_valid():
        #     form.save()
            
        #     with open('participants.csv', 'w', newline='') as csvfile:
        #             spamwriter = csv.writer(csvfile, delimiter=' ',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                       
        #             spamwriter.writerow(['name','branch','email','roll','phone','subit'])
        #             m_feilds=all_participants.values_list('name','branch','email','roll','phone','subit')
        #             for Participant in m_feilds:
        #                 spamwriter.writerow(Participant)      
        