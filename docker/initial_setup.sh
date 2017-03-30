echo "Creating django_waitlist_dev for Django 1.7"
docker-compose run --rm init-postgres17
echo "Running Migrations for Django 1.7"
docker-compose run --rm web17 python manage.py migrate
echo "Seeding DB for Django 1.7"
docker-compose run --rm web17 python manage.py loaddata waitlist_entries accounts
docker-compose stop

echo "Creating django_waitlist_dev"
docker-compose run --rm init-postgres
echo "Running Migrations"
docker-compose run --rm web python manage.py migrate
echo "Seeding DB"
docker-compose run --rm web python manage.py loaddata waitlist_entries accounts
docker-compose stop
