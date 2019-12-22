FROM nikolaik/python-nodejs:python3.7-nodejs13

RUN pip install Flask==1.0.2 Flask-Cors==3.0.7
RUN npm install -g @vue/cli@3.7.0

CMD ["/bin/bash"]
