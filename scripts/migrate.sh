cd /home/ubuntu/metalit
source /home/ubuntu/virtmetalit/bin/activate
export $(grep -v '^#' .env | xargs)
pip install --upgrade pip
if [ -e requirements.txt ]
then
    pip install -r requirements.txt
else
    echo "no requirements.txt"
fi
./manage.py migrate
