# python
FROM python:stretch

# setting the working directory
COPY . ./app
WORKDIR /app

# install python requirements
RUN pip install -r requirements.txt

EXPOSE 8080

# define an entrypoint which will run the main app using the Gunicorn WSGI server
ENTRYPOINT [ "python", "main.py"]
