# python
FROM python:stretch

# setting the working directory
COPY . ./harsh
WORKDIR /harsh

# install python requirements
RUN pip install -r requirements.txt

# EXPOSE 8080

# define an entrypoint which will run the main app using the Gunicorn WSGI server
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "main:APP"]
