# Project 2: Trivia App
---

This project is part of Udacity's Full Stack Nanodegree Program, wherein users can play a trivia game. Users can also
add new question, view all the question and select questions based on category. The learning objective is to understand
how API Development and Documentation.

All backend code follow PEP8 style guidelines.

## Getting Started
---

The project has decoupled frontend and backend. The frontend is written in React.js whereas the backend is written using Flask, a python webframework.

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
pip install -r requirements.txt
```

**Database Setup**

The backend assumes that Postgresql is used as the database. To install postgres on Ubuntu machine, follow the instruction [here](https://www.postgresql.org/download/linux/ubuntu/). Use google to search the instructions for installing the Postgresql on Windows or Mac. Once the Postgres is installed and running, create a database named 'trivia' using the following commands:

```bash
createdb trivia
```

With the database created, run the following command to run a script that creates the required tables and inserts some dummy data:

```bash
psql trivia < trivia.psql
```




```bash
$ export FLASK_APP=flaskr
$ export FLASK_DEBUG=true
$ flask run
``` 