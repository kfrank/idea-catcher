from django.http import HttpResponse
from django.shortcuts import render
from app import models
import json


def idea_list(request):
    ideas = models.Idea.objects.all()
    outputJSON = [idea.text for idea in ideas]
    return HttpResponse(json.dumps(outputJSON))

def new_idea(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        idea_text = request.POST['idea_text']
        if idea_text:
            idea = models.Idea(text=idea_text) 
            idea.save()
            return HttpResponse("Success")

def random(request):
    results = {}
    results["record"] = models.Idea.objects.order_by('?')[0].text
    results["response"] = models.Responses.objects.order_by('?')[0].text
    return HttpResponse(json.dumps(results))
