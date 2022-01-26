cd /home/ubuntu/metalit
source /home/ubuntu/virtmetalit/bin/activate
export $(cat .env | xargs) 
./manage.py collectstatic --noinput -i admin
