FROM django:onbuild

CMD "python app/manage.py runserver"
