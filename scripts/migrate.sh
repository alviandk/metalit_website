cd /home/ubuntu/myprojectdir
source /home/ubuntu/myprojectdir/myprojectenv/bin/activate
export $(grep -v '^#' .env | xargs)
pip install --upgrade pip
pip install -r requirements.txt
./manage.py migrate
