from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bot.processor import chatbot_response
# from . import settings

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
# print(settings.BASE_DIR)



def homepage(request):
    return render(request,"index.html")


@csrf_exempt
def newchat(request):
    if(request.method=="POST"):
        print(request.POST)
        question = request.POST['question']
        print(question)
        answer = chatbot_response(question)
        return JsonResponse({"response":answer})
    else:
        return JsonResponse({"Error":"Cannot execute given input"})