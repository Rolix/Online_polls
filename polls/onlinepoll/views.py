from django.template import Context, loader
from django.http import HttpResponse,HttpResponseRedirect
from models import Poll,Choice

def polls_list(request):
	poll_list=Poll.objects.all()
	t = loader.get_template('polls/list.html')
	c = Context({'polls_list':poll_list}),
	return HttpResponse(t.render(c))

def polls_detail(request,id):
	poll_detail= Poll.objects.get(id=id)
	choice = Choice.objects.filter(poll__id=id)
	if request.method == 'POST'
		return HttpResponse 'You just voted for '+str(choice.post.id)
	return HttpResponseRedirect('poll/detail/')
