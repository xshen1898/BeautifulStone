from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json

from .models import Lottery

# Create your views here.
def index(request):
    return render(request, 'index.html')

def save_lottery(request):
    if request.method == "POST":
        cellphone_num = request.POST.get('cellphone_num', '')
        award = request.POST.get('award', '')
        lottery = Lottery(cellphone_num=cellphone_num, award=award)
        lottery.save()
        return JsonResponse({'status':'success'})

def lottery_list(request):
    lottery = Lottery.objects.all()
    data = json.loads(serializers.serialize("json", lottery))
    return JsonResponse({'data': data})

def lottery_result(request):
    lottery_list = Lottery.objects.all()
    context = {'lottery_list': lottery_list}
    return render(request, 'lottery_result.html', context)
