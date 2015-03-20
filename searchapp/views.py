import os
import csv
import json

from django.shortcuts import render
from django.http import HttpResponse
from models import MPattendence

# Create your views here.
def home(request):
    params_dict =  get_url_params_dict(request.GET.iteritems())
    if params_dict:
        mp_data = MPattendence.objects.filter(**params_dict)
    else:
        mp_data = MPattendence.objects.all()
    return render(request, 'base.html', {"mp_data": mp_data, 
                    "params_dict": json.dumps(params_dict) if params_dict else None})


def get_url_params_dict(params):
    params_dict = {}
    for key, value in params:
        params_dict[key] = value
    return params_dict

def load_csv_data(request):
    filepath = "/home/hasher/workspace/workspace1/WebApp/sampleapp/searchapp/datafile.csv"
    csv_data = read_csv_data(filepath)
    for data in csv_data:
        if csv_data.index(data)!=0:
            mp_attendence_obj = MPattendence(division_or_seat_num=int(data['division_or_seat_num']),
                            member_name=data['member_name'].strip(), lok_sabha = int(data['lok_sabha']),
                            session=int(data['session']), state=data['state'].strip(), constituency=data['constituency'].strip(),
                            total_seats=int(data['total_seats']), num_of_days=0)
            mp_attendence_obj.save()
    return HttpResponse("Successfully uploaded csv file..")

def read_csv_data(filepath):
    fieldnames = ("S.No", "division_or_seat_num", "member_name", "lok_sabha",
                  "session", "state", "constituency", "total_seats", "num_of_days")
    try:
        csvfile = open(filepath, 'r')
    except:
        raise Exception("Not able to read the csv file.")
    reader = csv.DictReader(csvfile, fieldnames)
    csv_data = []
    for row in reader:
        csv_data.append(row)
    return csv_data
