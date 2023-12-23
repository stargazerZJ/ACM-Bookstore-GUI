# Deployment Guide
## 1. Install docker engine
To install docker, refer to [the official guide](https://docs.docker.com/engine/install/)
## 2. Build docker image
In the folder to which you download the code, run `docker build -t bookstore-gui .`
## 3. Run the bookstore server
Run the following
```bash
docker run \
	-p 80:5000 \
	-e PGID=$(id -g) \
	-e PUID=$(id -u) \
	-v /path/to/your/bookstore/database:/app/db:rw \
	bookstore-gui
```
**Replace** `/path/to/your/bookstore/database` with the path to the folder where you want to store the database.
You may need to run the command with `sudo` if you are not in the `docker` group.
## 4. Access the bookstore
Open your browser and go to `http://localhost`