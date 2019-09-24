#/ bin/bash
clear
#uwsgi --http-socket :10001 --wsgi-file test.py --master --threads 1 --processes 1 # for independent server
#uwsgi --http-socket :10001 --wsgi-file test.py --master --threads 1 --processes 1 # to plug into nginx

#uwsgi config.ini
uwsgi /home/jamie/website/jamieAndLivTempSite/serverCode/config.ini
