FROM django:onbuild

RUN python ./manage.py migrate

#CMD "python app/manage.py runserver"
