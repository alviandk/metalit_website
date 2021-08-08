cd /home/ubuntu/myprojectdir
source /home/ubuntu/myprojectdir/myprojectenv/bin/activate
export $(grep -v '^#' .env | xargs)
./manage.py migrate
