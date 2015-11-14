from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import datetime
from django.utils import timezone
from .serializers import QuestionSerializer
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def createPoll(request):
	return render(request, 'polls/create_poll.html')	

def newPoll(request):
	if request.method == "POST":
		q = Question(question_text=request.POST['name'], pub_date=timezone.now())
		q.save()

		c = Choice(question = q, choice_text = request.POST['option1'], votes=request.POST['votes1'])
		c.save()

		c = Choice(question = q, choice_text = request.POST['option2'], votes=request.POST['votes2'])
		c.save()

		c = Choice(question = q, choice_text = request.POST['option3'], votes=request.POST['votes3'])
		c.save()

	return HttpResponse("Poll created")

def deletePoll(request):
	poll_list = Question.objects.order_by('-pub_date')
	context = { 'poll_list' : poll_list }
	return render(request, 'polls/delete_poll.html',context)	

def deleteOnePoll(request):

	try:
	    q = Question.objects.get(pk=request.POST['poll'])
	except (KeyError, Question.DoesNotExist):
		return render(request, 'polls/delete_poll.html', {
			'error_message': "Select a poll.",})
	else:
		q.delete()
		return HttpResponse("Poll deleted")

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))



class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def polls(request):

	if request.method == 'GET':
		encuestas = Question.objects.all()
		serializador = QuestionSerializer(encuestas, many=True)
		return JSONResponse(serializador.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = QuestionSerializer(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
	return JSONResponse(serializador.errors, status=400)













