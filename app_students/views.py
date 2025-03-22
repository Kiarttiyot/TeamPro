from django.shortcuts import render
from django.http.response import HttpResponse
from .models import GoogleSheetData
from .google_sheets import df

def sync_google_sheet_data():
    GoogleSheetData.objects.all().delete()
    for _, row in df.iterrows():
        birthdate = row.get('Birthdate', '')  
        GoogleSheetData.objects.create(
            D = row['D'],    
            email=row['email'],
            years = row['years'],
            student_id=row['student_id'],
            title=row['title'],
            name=row['name'],
            gender=row['gender'],
            phone=row['phone'],
            nickname = row['nickname']
        )

# Create your views here.
def ce01s(request):
    sync_google_sheet_data()
    ce01s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce01s.html',{'ce01s':ce01s})
def ce02s(request):
    sync_google_sheet_data()
    ce02s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce02s.html',{'ce02s':ce02s})
def ce03s(request):
    sync_google_sheet_data()
    ce03s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce03s.html',{'ce03s':ce03s})
def ce04s(request):
    sync_google_sheet_data()
    ce04s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce04s.html',{'ce04s':ce04s})

def ce01(request, ce01D):
    sync_google_sheet_data()  # Sync data if necessary
    try:
        one_ce01 = GoogleSheetData.objects.get(D=ce01D)  # Fetch the object directly from the model
    except GoogleSheetData.DoesNotExist:
        one_ce01 = None  # Handle the case where the object does not exist
    context = {'ce01': one_ce01}
    return render(request, 'app_students/ce01.html', context)
def ce02(request,ce02D):
    sync_google_sheet_data()  # Sync data if necessary
    try:
        one_ce02 = GoogleSheetData.objects.get(D=ce02D)  # Fetch the object directly from the model
    except GoogleSheetData.DoesNotExist:
        one_ce02 = None  # Handle the case where the object does not exist
    context = {'ce02': one_ce02}
    return render(request, 'app_students/ce02.html', {'ce02D': ce02D})
def ce03(request,ce03D):
    sync_google_sheet_data()  # Sync data if necessary
    try:
        one_ce03 = GoogleSheetData.objects.get(D=ce03D)  # Fetch the object directly from the model
    except GoogleSheetData.DoesNotExist:
        one_ce03 = None  # Handle the case where the object does not exist
    context = {'ce03': one_ce03}
    return render(request, 'app_students/ce03.html', {'ce03D': ce03D})
def ce04(request,ce04D):
    sync_google_sheet_data()  # Sync data if necessary
    try:
        one_ce04 = GoogleSheetData.objects.get(D=ce04D)  # Fetch the object directly from the model
    except GoogleSheetData.DoesNotExist:
        one_ce04 = None  # Handle the case where the object does not exist
    context = {'ce04': one_ce04}
    return render(request, 'app_students/ce04.html', {'ce04D': ce04D})