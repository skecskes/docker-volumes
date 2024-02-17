# Docker volumes

Run locally:

    pip install -r requirements.txt
    uvicorn main:app --host=0.0.0.0 --port=80

Create docker image:
    
    docker build -t my-app .

Run docker image:

    docker run -d -p 80:80 --name my-app-container my-app 

Stop docker container:

    docker stop my-app-container

Remove docker container:

    docker rm my-app-container

Remove docker image:

    docker rmi my-app

