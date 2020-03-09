import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
import ipdb
print('message at the top after imports')


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        # ipdb.set_trace()
        print('inside func: setup')
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
        ipdb.set_trace()
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ######################################
    # tests for endpoint: get_questions
    ######################################

    ######################################
    # tests for endpoint: delete_questions
    ######################################

    ######################################
    # tests for endpoint: add_question
    ######################################

    ######################################
    # tests for endpoint: search_question
    ######################################

    ######################################
    # tests for endpoint: category_questions
    ######################################

    ######################################
    # tests for endpoint: play_quiz
    ######################################


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
