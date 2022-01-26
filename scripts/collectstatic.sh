cd /home/ubuntu/metalit
source /home/ubuntu/virtmetalit/bin/activate
export $(cat .env | xargs) 
if [ -d static ]
then
    excho "static dir exist"
else
    mkdir static
cd /home/ubuntu/metalit/static
git fetch origin
reslog=$(git log HEAD..origin/main --oneline)
if [[ "${reslog}" != "" ]] ; then
    git pull origin main
    cd /home/ubuntu/metalit
    ./manage.py collectstatic --noinput -i admin -i ckeditor -i graphene_django -i rest_framework
