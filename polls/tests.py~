import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice

# Create your tests here.

class QuestionMethodTests(TestCase):


	def test_votes(self):
		q = Question(question_text = "Test question",pub_date=timezone.now())



		c = Choice(question = q , choice_text = "Choice test 1", votes=2)

		self.assertEqual(c.votes, 2)
		print"Test: Comprobacion votos"

	def test_create_question(self):
		q = Question(question_text = "Test question",pub_date=timezone.now())

		q.save()

		c = Choice(question = q , choice_text = "Choice test 1", votes=2)

		c.save()

		c = Choice(question = q , choice_text = "Choice test 2", votes=6)

		c.save()

		c = Choice(question = q , choice_text = "Choice test 3", votes=8)

		c.save()

		
		self.assertEqual(q.question_text, "Test question")
		print"Test: Creacion y salvado de encuestas con opciones"

	def test_was_published_recently_with_future_question(self):
 
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)
		print"Test: Comprobacion fecha de creacion"

	def test_polls(self):
		q = Question(question_text = "Cuestion1",pub_date="2010-11-11")
		q.save()
		q = Question(question_text = "Cuestion2",pub_date="2010-11-11")
		q.save()
		response = self.client.get('/polls/')
		self.assertEqual(response.content,'[{"question_text":"Cuestion1","pub_date":"2010-11-11"},{"question_text":"Cuestion2","pub_date":"2010-11-11"}]')

		print"Test: Vista JSON"


		





