# -*- coding: utf-8 -*-
from django.test import TestCase
from Tutorial2.models import Question
from django.utils import timezone


class QuestionModelTest(TestCase):
    def test_save_and_retrieve(self):
        # when
        question = Question.objects.create(question_text=u'우리 나라 이름은?', pub_date=timezone.now()) #1 
        
        # then
        self.assertEqual(Question.objects.count(), 1) #2
        actual = Question.objects.first() #3
        self.assertEqual(question, actual) #4


class QuestionViewTest(TestCase):
    def test_uses_questions_template(self):
        # when
        response = self.client.get('/questions') #1
        
        # then
        self.assertEqual(response.status_code, 200) #2
        self.assertTemplateUsed(response, 'questions.html') #3
    
    def test_displays_questions(self):
        # given
        Question.objects.create(question_text=u'우리 나라 이름은?', pub_date=timezone.now()) #1
        Question.objects.create(question_text=u'우리 나라 수도는?', pub_date=timezone.now())
        
        # when
        response = self.client.get('/questions') #2
        
        # then
        self.assertContains(response, u'우리 나라 이름은?') #3
        self.assertContains(response, u'우리 나라 수도는?')
    
    def test_can_save_a_POST_request(self):
        # when
        self.client.post('/questions/add', data={'question_text': u'우리 나라 이름은?'}) #1
        
        # then
        self.assertEqual(Question.objects.count(), 1) #2
        new_question = Question.objects.first() #3
        self.assertEqual(new_question.question_text, u'우리 나라 이름은?') #4
    
    def test_redirects_after_POST(self):
        # when
        response = self.client.post('/questions/add', data={'question_text': u'우리 나라 이름은?'}) #1
        
        # then
        self.assertEqual(response.status_code, 302) #2
        self.assertRedirects(response, '/questions') #3