rsync -zvh emperor.uwsgi.service /etc/systemd/system/
systemctl daemon-reload
echo "Restarting: emperor.uwsgi.service"
sudo systemctl restart emperor.uwsgi.service
