# Sample Application

## Requirements
* Docker-compose
* Django=>3.1 python=>3.9

## Deploy

#### Install docker-compose
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
sudo apt install docker-ce
sudo usermod -aG docker ${USER}
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Clone repository
```bash
git clone git@github.com:IlyaSpirkov/python-django-sample-app.git
```
#### Build docker images
```bash
cd sample # move to directory with docker-compose.yaml
docker-compose -f docker-compose.yaml up --build # download requirements, build images, apply migrations and run server
```
There are 5 container:
1. app (contains django project)
2. db (contains postgres db)
3. redis
4. celery
5. celery-beat

#### Initial setup
```bash
docker-compose -f docker-compose.prod.yaml exec web python manage.py migrate # run migrations for DB
docker-compose -f docker-compose.prod.yaml exec web python manage.py collectstatic # collect static files (for admin-panel)
```

#### Shut down containers
```bash
docker-compose -f docker-compose.yaml down -v
```

#### Create super user for accessing admin panel
```bash
docker-compose -f docker-compose.prod.yaml exec web python manage.py createsuperuser
```

## Main Info
#### Base API for working with user accounts, where you can:
- register and remove user accounts
- authorize and logout user accounts
- get/update user profile
- set profile avatar
