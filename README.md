# Docker volumes

This repository is helper for the article [Docker volumes](https://skey.uk/post/docker-volumes/).

## Basic commands

Run locally:

    pip install -r requirements.txt
    uvicorn main:app --host=0.0.0.0 --port=80

Create docker image called `my-app` based on the `Dockerfile` in the current directory:
    
    docker build -t my-app .

Run docker container called `my-app-container` based on the `my-app` image on port 80:

    docker run -d -p 80:80 --name my-app-container my-app 

Stop docker container:

    docker stop my-app-container

Remove docker container:

    docker rm my-app-container

Remove docker image:

    docker rmi my-app

Check volumes:

    docker volume ls

Remove volume with name `named-volume`:

    docker volume rm named-volume

## Run anonymous volume

    docker build -t my-app -f anon-volume.Dockerfile .
    docker run -d -p 80:80 --rm --name my-app-container my-app
    
The above will use `VOLUME /app/temp` from the `Dockerfile` to create an anonymous volume. But you can also create 
an anonymous volume when starting the container:

    docker run -d -p 80:80 --rm --name my-app-container -v /app/temp my-app

## Run named volume

    docker build -t my-app .
    docker run -d -p 80:80 --rm --name my-app-container -v named-volume:/app/temp  my-app 

The volume called `named-volume` will be created automatically if it does not exist.

## Run bind mount

    docker build -t my-app -f bind-mount.Dockerfile .
    docker run -d -p 80:80 --rm --name my-app-container -v named-volume:/app/temp -v $(pwd):/app my-app

The above will mount the current directory to `/app` in the container. and for temp folder it will create/reuse the 
`named-volume` volume. Check the `bind-mount.Dockerfile` to see that we don't copy the source files to image and
that we use `--reload` flag for `uvicorn` to reload the server when the source files change.
