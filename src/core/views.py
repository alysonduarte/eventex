#from django.shortcuts import render_to_response
#from django.template import RequestContext

#def homepage(request, template=None):
#    return render_to_response(template, RequestContext(request))

from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    from django.conf import settings
    context = {'STATIC_URL': settings.STATIC_URL}

    return render_to_response('index.html', context)


#def homepage(request):
#    t = loader.get_template(index.html)
#    c = Context();
#    
#    content = t.render(c)
#    
#    return HttpResponse(content)