from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    content = {
        'content':[{'id':'1','name':'cristiano','date':'today',},
                   {'id':'2','name':'camavinga','date':'last day',},
                   {'id':'3','name':'vini jr','date':'last week',},
                   {'id':'4','name':'rafa','date':'last month',},
                    ]
    }
    
    return render(request=request,template_name='post.html',context=content)
# Create your views here.
