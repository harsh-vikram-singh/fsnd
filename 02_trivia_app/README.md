# Project 2: Trivia App

This project is part of Udacity's Full Stack Nanodegree Program, wherein users can play a trivia game. Users can also
add new question, view all the question and select questions based on category. The learning objective is to understand
how API Development and Documentation.

All backend code follow PEP8 style guidelines.

## Getting Started

The project has decoupled frontend and backend. The frontend is written in React.js whereas the backend is written using Flask, a python webframework.

--- 

### Running the backend

To run the backend:

#### Installing dependencies

**Python 3.7**

Follow instructions to install Python3.7 or above from the [Python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

**Virtual Environment**

Create a new virtual environment to avoid conflicts from your other virtual environment. Instructions to create new virtual environment can be found in
the [Python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

**Pip Dependencies**

Once the virtual environment is setup and activated, the dependencies required for the project can be installed using the following command:
```bash
$ pip install -r requirements.txt
```

**Database Setup**

The backend assumes that Postgresql is used as the database. To install postgres on Ubuntu machine, follow the instruction [here](https://www.postgresql.org/download/linux/ubuntu/). Use google to search the instructions for installing the Postgresql on Windows or Mac. Once the Postgres is installed and running, create a database named 'trivia' using the following commands:

```bash
$ createdb trivia
```

With the database created, run the following command to run a script that creates the required tables and inserts some dummy data:

```bash
$ psql trivia < trivia.psql
```

**Running the Flask app**

Run the following commands in your virtual environment to run the flask app in development mode:

```bash
$ export FLASK_APP=flaskr
$ export FLASK_DEBUG=true
$ flask run
``` 
--- 

### Running the Frontend

#### Installing dependencies

##### Installing Node and npm

Node and node package manager(npm) are required to run the frontend. These can be installed from [here](https://nodejs.com/en/download)

##### Installing project dependencies

Navigate to the project website and run the following command:

```bash
$ npm install
```

##### Running the frontend in development mode

Run the following command:

```bash
$ npm start
```

This would start a dev server for the frontend. In your web browser, navigate to the following link to view the frontend:

[http://localhost:3000](http://localhost:3000)

---

### Running the Tests

The project uses the python library unittest to create and run a test suite for testing the various endpoints. In order to run tests, navigate to the backend folder and run the following commands:

```bash
$ dropdb trivia_test
$ createdb trivia_test
$ psql trivia_test < trivia.psql
$ python test_flaskr
```

**Note**: In case running `python test_flaskr` results in a message like: `Ran 0 tests in 0.000s`, run the tests with following command:
`python -m  unittest discover -s .`

If running the tests for the first time, omit the 'dropdb trivia_test' command. These commands reset the database and populate the tables with some dummy data, on which the defined endpoints can be tested. Also, ensure that these commands are run in the proper virtual environment.

---

## API Reference

### Getting Started

* Base URL: At present, this app can only be run locally. The backend is hosted at the default `http://localhost:5000`, which is set as a proxy in the frontend configuration.
* Authentication: For this version of the app, authentication is not implemented.

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
    "success": false,
    "error": 400,
    "message": "Bad Request"
}
```

The API will return the following three error types when requests fail:

* 400: Bad Request
* 404: Not Found
* 422: Can not be processed. Please check your request again

### Endpoints

#### GET /categories

* General

    * Returns a list of all the categories of the questions in the database

* Sample request:  `curl localhost:5000/categories`

* Sample response:

```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true
}
```

#### GET /questions

* General
    * Returns total_questions, success status and lists of categories and questions
    * The results are paginated with 10 questions per page

* Sample requests:
    `curl localhost:5000/questions` for the first page, or `curl localhost:5000/questions?page=2`

* Sample response:

```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist's initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 21
}
```

#### POST /questions

* General
    * Add a new question in the database
    * Required fields: question, answer, category and difficulty. All are required to successfully add a question to the database.
    * Once the question is added, the server returns total_questions, success status and lists of categories and questions
    * The list of questions is paginated, with maximum 10 questions per page

* Sample request:
`curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is the author of: A Game of Thrones", "answer": "G. R. R. Martin", "category": 4, "difficulty": 2}' localhost:5000/questions`

* Sample response:
```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist's initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 22
}
```

#### DELETE /questions/{question_id}

* General
    * Deletes a question using the question id.
    * Once the question is deleted, the server returns total_questions, success status and lists of categories and questions.
    * The list of questions is paginated, with maximum 10 questions per page.

* Sample request: `curl -X DELETE localhost:5000/questions/5`

* Sample response:
```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist's initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }
  ], 
  "success": true, 
  "total_questions": 21
}
```

#### POST /questions/search

* General
    * Search questions based on a search term.
    * The endpoint returns all the questions for whom the search term is a substring of the question (search is case-insensitive)
    * The questions list will update to include only question that include that string within their question.
    * the server returns total_questions that match the search criteria, success status and lists of categories and questions that match the search criteria.

* Sample request:
`curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "thrones"}' localhost:5000/questions/search`

* Sample response:
```json
{
  "current_category": null, 
  "questions": [
    {
      "answer": "G. R. R. Martin", 
      "category": 4, 
      "difficulty": 2, 
      "id": 63, 
      "question": "Who is the author of: A Game of Thrones"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```

#### GET /categories/{category_id}/questions

* General
    * Returns all the questions for a particular category
    * Server response includes success status, number of total questions for the category that was searched and a list of questions that belong to that category

* Sample request: `curl localhost:5000/categories/{category_id}/questions` where {category_id} should be replaced by the id of the category being searched. For example: `curl localhost:5000/categories/3/questions`

* Sample response:
```json
{
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

#### POST /quizzes

* General
    * Returns questions to play the quiz.
    * Takes category and previous_question parameter.
    * Returns a random question within the given category.
    * Ensures that the question being returned is not in the previous_question parameter

* Sample request:
`curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [6], "quiz_category": {"type": 3, "id": 2}}' localhost:5000/quizzes`

* Sample response:
```json
{
  "question": {
    "answer": "The Palace of Versailles", 
    "category": 3, 
    "difficulty": 3, 
    "id": 14, 
    "question": "In which royal palace would you find the Hall of Mirrors?"
  }, 
  "success": true
}
```
---

## Deployment

Not applicable

## Author

Harsh Vikram Singh

## Acknowledgements

Instructions to install various dependencies were taken from Udacity's readme file for the backend as well as frontend.

The Structure of this README was inspired from the Coach Caryn's video on API Documentation.
