FROM nikolaik/python-nodejs:python3.7-nodejs13

RUN pip install Flask==1.0.2 Flask-Cors==3.0.7
RUN npm install -g @vue/cli@4.1.1
RUN npm install axios@0.18.0 vuetify@2.1.15

CMD ["/bin/bash"]
