# Apache Superset Dashboard Thumbnails

How to enable thumbnails in superset 1.0.1
## Installation



```bash
git clone https://github.com/Akitha/superset-thumbnails.git

cd superset-thumbnails/
```

## Usage
1. Running this Docker build
```bash
docker build -t superset-1.0.1-extended -f Dockerfile .
```
2. Run the image using docker-compose up
```bash
docker-compose up 
```
3. In a new terminal window, upgrade the DB
```bash
docker exec -it superset-1.0.1-extended superset db upgrade
```
4. Then run 
```bash
docker exec -it superset-1.0.1-extended superset init
```
5. Then setup your admin user
```bash
docker exec -it superset-1.0.1-extended superset fab create-admin
```
6. Finally, restart the running instance
```bash
CTRL-C
docker-compose up

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
