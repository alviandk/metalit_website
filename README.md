# Metalit Website

## How to run on local machine
* mkdir metalit
* cd metalit
* git clone https://github.com/alviandk/metalit_website.git
* virtualenv -p python3 virtmetalite
* source virtmetalite/bin/activate
* cd metalit_website
* pip install -r requirements.txt
* git branch [nama branch]
* git checkout [nama branch]

* add export virtualenviroment variabel to virtmetalite/bin/activate
```
export SECRET_KEY='abcd'
export DJANGO_DEBUG=True
export ALLOWED_HOSTS=127.0.0.1
export BLOG_URL=http://localhost:3000

export OSS_ACCESS_KEY_ID=<ask admin>
export OSS_ACCESS_KEY_SECRET=<ask admin>
export OSS_BUCKET_NAME=<ask admin>
export OSS_ENDPOINT=<ask admin>
```

* source ../virtmetalite/bin/activate
* python manage.py migrate
* python manage.py runserver
