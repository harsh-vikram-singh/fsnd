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

#### POST /questions

#### DELETE /questions/{question_id}

#### POST /questions/search

#### GET /categories/{category_id}/questions

#### POST /quizzes