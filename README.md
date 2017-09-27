# Excursus

A discussions portal

## Getting Started

Clone or fork the repo to make changes and test the portal.

### Prerequisites

Install django, redis, django-channels (as the final project will be realtime) and PostgreSQL.


### Installing

Create a vitual enviroment if you have deal with multiple pyhton projects.

```
sudo apt-get install python-virtualenv
or
sudo easy_install virtualenv
or
sudo pip3 install virtualenv
```

```
mkdir ~/virtualenvironment
virtualenv ~/virtualenvironment/my_new_app
cd ~/virtualenvironment/my_new_app/bin
source activate
```

To install django, channels and redis.
Note: Use sudo only if some errors pop up.

```
sudo pip3 install django
sudo pip3 install channels
sudo apt-get install redis-server
sudo pip3 install asgi_redis
```

Follow [these instructions](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) to run PostgreSQL database.
PostgreSQL provides much better searching, indexing and scaliblity options.

Configure your Database settings in settings.py to run the database. Assign DEBUG False and configure the Apache/Nginx to host the django app, PostgreSQL database and required static files.

Finally run

```
python3 manage.py runserver
```

in the directory which has manage.py to get your portal up and running.


## Built With

* HTML5
* [Bootstrap v4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - For enchancing look and responsiveness of website
* [Now-ui-kit](http://demos.creative-tim.com/now-ui-kit/presentation.html) - A custom bootstrap theme
* [jQuery](https://jquery.com/) - A feature-rich Javascript library
* [Django](https://www.djangoproject.com/) - A python-based web framework
* [Django-channels](https://channels.readthedocs.io/en/stable/) - For realtime changes
* [Redis](https://redis.io/) - To store django-channels passed messages
* [PostgreSQL](https://www.postgresql.org/) -  A powerful, open source object-relational database system
* [Hardwork](https://www.google.co.in/search?source=hp&q=hard+work+meaning&oq=hard+work+&gs_l=psy-ab.3.0.0i67k1l4.613.2084.0.2841.5.4.0.0.0.0.238.514.0j2j1.3.0....0...1.1.64.psy-ab..2.3.511.0..35i39k1.0.QbCZoSQ6rCk) :p

## Contributing

TODO

## Authors

* **Vivek Raj**  - [Excursus](https://github.com/codervivek/excursus)

## License

TODO


