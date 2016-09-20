docker-compose up -d postgreshost
echo "WAITING FOR DATABASE TO START"
sleep 4 # wait for the database to start up
echo "CREATING django_waitlist_dev"
docker-machine ip | xargs -I % psql -h % -p 5432 -d postgres -U postgres -c 'create database django_waitlist_dev'
echo "Running Migrations"
docker-compose run web python manage.py migrate
echo "Seeding DB"
docker-compose run web python manage.py loaddata waitlist_entries accounts
docker-compose stop
