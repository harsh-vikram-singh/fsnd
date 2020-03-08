import os
from flask import Flask, request, abort, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import ipdb
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

    '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
    @app.route('/categories')
    def get_all_categories():
        categories = Category.query.all()
        formatted_categories = [category.format() for category in categories]
        # print(formatted_categories)
        return jsonify({
            'success': True,
            'categories': formatted_categories
        })
    '''
  @TODO:
  Create an endpoint to handle GET requests for questions,
  including pagination (every 10 questions).
  This endpoint should return a list of questions,
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions.
  '''
    @app.route('/questions')
    def get_questions():
        print('endpoint: get_questions')
        page = request.args.get('page', 1, type=int)
        questions = Question.query.paginate(page=page, per_page=10)
        questions_list = questions.items
        formatted_questions = [question.format()
                               for question in questions_list]
        categories = Category.query.all()
        formatted_categories = [category.format() for category in categories]

        return jsonify({
            'success': True,
            'questions': formatted_questions,
            'total_questions': questions.total,
            'current_category': None,
            'categories': formatted_categories,
        })

    '''
  @TODO:
  Create an endpoint to DELETE question using a question ID.

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page.
  '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        # ipdb.set_trace()
        try:
            question = Question.query.get(question_id)

            if question is None:
                abort(404)

            question.delete()
            questions = Question.query.paginate(page=1, per_page=10)
            questions_list = questions.items
            formatted_questions = [question.format()
                                   for question in questions_list]
            categories = Category.query.all()
            formatted_categories = [category.format()
                                    for category in categories]

            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': questions.total,
                'current_category': None,
                'categories': formatted_categories
            })
        except:
            abort(404)

    '''
  @TODO:
  Create an endpoint to POST a new question,
  which will require the question and answer text,
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab,
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.
  '''
    @app.route('/questions', methods=['POST'])
    def add_question():
        print('endpoint hit: add_question, method: POST')
        try:
            data = request.get_json()
        except:
            abort(400)

        question_text = data.get('question')
        answer = data.get('answer')
        difficulty = data.get('difficulty')
        category = data.get('categoty')

        print(question_text)

        question = Question(question=question_text,
                            answer=answer,
                            category=category,
                            difficulty=difficulty)
        try:
            question.insert()
        except:
            abort(422)

        questions = Question.query.paginate(page=1, per_page=10)
        questions_list = questions.items
        formatted_questions = [question.format()
                               for question in questions_list]
        categories = Category.query.all()
        formatted_categories = [category.format() for category in categories]

        return jsonify({
            'success': True,
            'questions': formatted_questions,
            'total_questions': questions.total,
            'current_category': None,
            'categories': formatted_categories,
        })

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
    @app.route('/questions/search', methods=['POST'])
    def search_question():
        data = request.get_json()
        search_term = data.get('searchTerm')
        questions = Question.query.filter(
            Question.question.ilike(f'%{search_term}%')).all()
        formatted_questions = [question.format() for question in questions]
        print(formatted_questions)
        return jsonify({
            'success': True,
            'current_category': None,
            'questions': formatted_questions,
            'total_questions': len(questions)
        })
    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

    return app
