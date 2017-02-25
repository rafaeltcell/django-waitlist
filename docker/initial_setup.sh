: ${DOCKER_IP:?"needs to be set in your env (ex: export DOCKER_IP=0.0.0.0)"}

docker-compose up -d postgreshost
echo "WAITING FOR DATABASE TO START"
sleep 4 # wait for the database to start up
echo "CREATING django_waitlist_dev"
psql -h $DOCKER_IP -p 5432 -d postgres -U postgres -c 'create database django_waitlist_dev'
echo "Running Migrations"
docker-compose run --rm web python manage.py migrate
echo "Seeding DB"
docker-compose run --rm web python manage.py loaddata waitlist_entries accounts
docker-compose stop
