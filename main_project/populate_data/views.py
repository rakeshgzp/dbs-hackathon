from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
# import hashlib,json,details.connect,datetime,base64,requests,os,random,ast,details.encode
from collections import OrderedDict
from django.contrib.auth.decorators import login_required 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .models import customer_list,customer_values,rules,decision

class retrieve_id(APIView):
    def get(self,request,uid):
        try:
            profile = get_object_or_404(customer_list, uid=uid)
            # print(profile)
            new_profile = {
                "uid":profile.uid,
                "name":profile.name,
                "dob":profile.dob,
                "loan":profile.loan,
                "email":profile.email,
                "mobile":profile.mobile

            }
            return Response(new_profile)
        except Exception as e:
            return Response({"msg":"uid Not found"})


class update_id(APIView):
    def post(self,request):
        try:
            uid = request.data['uid']
            customer_list.objects.filter(uid=uid).update(name=request.data['name'],
            dob=request.data['dob'],loan=request.data['loan'],email=request.data['email'],
            mobile=request.data['mobile'])        
            return Response({"msg":"Success"})
        except Exception as e:
            return Response({"msg":"Some error"})    

class customer_item(APIView):
    def get(self,request,uid):
        try:
            profile = get_object_or_404(customer_values,uid = int(uid))
            data = {"name":profile.name,"ubill_value":profile.ubill_value,"tchallan_value":profile.tchallan_value,
            "ecar_value":profile.ecar_value,"penalty_value":profile.penalty_value}
            return Response(data)
        except Exception as e:
            return Response({"msg":"UID not found"})

class update_customer_ivalue(APIView):
    def post(self,request):
        try:
            uid = request.data['uid']
            # print(name=request.data['name'],ubill_value=request.data['ubill_value'],
            # tchallan_value=request.data["tchallan_value"],ecar_value=request.data['ecar_value'],penalty_value=request.data['penalty_value'])
            customer_item.objects.filter(uid=uid).update(name=request.data['name'],ubill_value=request.data['ubill_value'],
            tchallan_value=request.data["tchallan_value"],ecar_value=request.data['ecar_value'],penalty_value=request.data['penalty_value'])        
            return Response({"msg":"Success"})
        except Exception as e:
            return Response({"err":e})    

class show_score(APIView):
    def get(self,request,uid):
        try:
            values = get_object_or_404(customer_values,uid = int(uid))
            ubill_value,tchallan_value,ecar_value,penalty_value = values.ubill_value,values.tchallan_value,values.ecar_value,values.penalty_value
            comp_values = get_object_or_404(rules,rule_id=1)
            score = 0
            if (ubill_value>comp_values.ubill_value):
                print(score)
                score += ubill_value*comp_values.ubill_wt
            if (tchallan_value>comp_values.tchallan_value):
                print(score)
                score += tchallan_value*comp_values.tchallan_wt
            if (ecar_value>comp_values.ecar_value):
                print(score)
                score += ecar_value*comp_values.ecar_wt
            if (penalty_value>comp_values.penalty_value):
                print(score)
                score += penalty_value*comp_values.penalty_wt
            if score>0:
                decision.objects.create(uid=uid,score=score,status="True")
                return Response({"Result":"Yes","Score":score})
            else:
                decision.objects.create(uid=uid,score=score,status="False")
                return Response({"Result":"No","Score":score})
            # return HttpResponse("Score")

        except Exception as e:
            return HttpResponse(e)