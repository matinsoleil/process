# Simple Python Controller Api
Python api Controller

from https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

. bin/activate

gunicorn -b 0.0.0.0:5000 main:app --reload
