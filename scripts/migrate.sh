cd /home/ubuntu/metalit_website
source /home/ubuntu/virtmetalit/bin/activate
export $(grep -v '^#' .env | xargs)
pip install --upgrade pip
