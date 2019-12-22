FROM nikolaik/python-nodejs:python3.7-nodejs13

RUN pip install Flask==1.0.2 Flask-Cors==3.0.7

CMD ["/bin/bash"]
