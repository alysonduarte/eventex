
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request) 
    else:
        return new(request)

def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form':form})
    return render_to_response('subscriptions/new.html', context)

def create(request):
    form = SubscriptionForm(request.post)
    
    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('subscriptions/new.html', context)
    
    subscription = form.save()
    return HttpResponseRedirect(reverse('subscriptions:success', args=[subscription.pk]))

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscriptions/success.html', context)