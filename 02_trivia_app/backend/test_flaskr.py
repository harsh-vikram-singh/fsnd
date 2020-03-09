import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
import ipdb


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    # ipdb.set_trace()

    def setUp(self):
        # ipdb.set_trace()
        # print('inside func: setup')
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://postgres:postgres@{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'Who is Iron Man',
            'answer': 'Tony Stark',
            'category': 5,
            'difficulty': 5
        }

        self.search_term = {
            'searchTerm': 'autobiography'
        }

        self.play_quiz = {
            'previous_questions': [],
            'quiz_category': {
                'type': 1,
                'id': 0
            }
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    ######################################
    # tests for endpoint: get_all_categories
    ######################################

    def test_get_all_categories(self):
        # ipdb.set_trace()
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    ######################################
    # tests for endpoint: get_questions
    ######################################
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    ######################################
    # tests for endpoint: add_question
    ######################################
    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    ######################################
    # tests for endpoint: delete_questions
    ######################################
    def test_delete_questions(self):
        res = self.client().delete('/questions/9')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
    ######################################
    # tests for endpoint: search_question
    ######################################

    def test_search_question(self):
        res = self.client().post('/questions/search', json=self.search_term)
        data = json.loads(res.data)
        # ipdb.set_trace()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    ######################################
    # tests for endpoint: category_questions
    ######################################
    def test_category_questions(self):
        res = self.client().get('/categories/6/questions')
        data = json.loads(res.data)
        # ipdb.set_trace()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    ######################################
    # tests for endpoint: play_quiz
    ######################################
    def test_play_quiz(self):
        res = self.client().post('/quizzes', json=self.play_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
