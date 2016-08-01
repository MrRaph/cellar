# Cellar

I'm trying to learn about wine and I want to track what I like
and don't like. This is a small app that I can use to track bottles
in my cellar (aka my bookshelf).

Why not use an existing service? I don't really care what anybody else
thinks about wine, I just want to remember what I'm opening and where I
got it.

Starting small right now. The only interface is Django's admin because
it does basically everything I need it to. I will probably put some sort
of RESTful API or something up to interact with it from my phone but I'm
not sure how that will work yet.

# Install


## On Fedora

sudo dnf install postgresql-devel redhat-rpm-config python3-devel mariadb-devel
mkvirtualenv cellar
pip install -r requirements.txt


./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver


## On Docker

### Docker 1.12 with Services

Here is the command I used to create my Service :

    docker service create --name techan_wine \
    --restart-condition any \
    --network frontend \
    --endpoint-mode dnsrr \
    --update-delay 30s \
    --replicas 2 \
    mrraph/my-cellar


If you want to use SQLite, add the following line to the `docker service create` command :

    --mount type=bind,source=/data/cellar/db.sqlite3,target=/usr/src/app/app/db.sqlite3 \

If you want to use MySQL, add the following line to the `docker service create` command :


    --env DATABASE_URL=mysql://MYSQL_USER_NAME:MYSQL_USER_PASS@MYSQL_HOST:MYSQL_PORT/DB_NAME


Then, run the following commands after the service starts for the first time.

    docker exec -it techan_wine.2.4ex0w9hqaf8irjg1m4v3hjnqb ./manage.py makemigrations
    docker exec -it techan_wine.2.4ex0w9hqaf8irjg1m4v3hjnqb ./manage.py migrate
    docker exec -it techan_wine.2.4ex0w9hqaf8irjg1m4v3hjnqb ./manage.py createsuperuser
