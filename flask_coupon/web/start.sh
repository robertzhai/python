echo " restart service ..."
ps aux | grep gunicorn | awk '{print $2;}' | xargs kill -9
ps aux | grep supervisor | awk '{print $2;}' |  xargs kill -9
sleep 1
supervisord  -c conf/supervisor.conf
echo "deone"
