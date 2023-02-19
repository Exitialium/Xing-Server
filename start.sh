sudo /opt/bitnami/ctlscript.sh stop
sudo pkill -9 -f manage.py
sudo python /home/bitnami/Xing-server/manage.py runserver 0.0.0.0:80
