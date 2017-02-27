echo "Creating django_waitlist_dev"
docker-compose run --rm init-postgres
echo "Running Migrations"
docker-compose run --rm web python manage.py migrate
echo "Seeding DB"
docker-compose run --rm web python manage.py loaddata waitlist_entries accounts
docker-compose stop
