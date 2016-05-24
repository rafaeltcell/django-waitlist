# django_waitlist

### Docker Images
- web
- tcell_web

### Setup

1.  ```docker-compose build```
2.  ```sh docker/initial_setup.sh``` # needs `psql`. creates db and seeds it.
3.  ```docker-compose up web``` or ```docker-compose up tcell_web```

### Vulnerabilities

* `http://host:port/vulnerabilities/search`  
Input from search form is executed raw in the db thereby creating a security hole

* `http://host:port/vulnerabilities/sql_exception/`  
Raw sql is malformed so it will raise an sql exception
