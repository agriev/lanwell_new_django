<h1>Lanwell </h1>


Launch script in production
<code>
./env/bin/uwsgi --master --die-on-term --chdir=/var/www/lanwell_new/ --module=lanwell_new_django.wsgi:application --http=0.0.0.0:8000 --buffer-size=64000 --processes 4
</code>