# Docker volumes

Run locally:

    pip install -r requirements.txt
    uvicorn main:app --host=0.0.0.0 --port=8080

Create docker image:
    
    docker build -t myapp .

Run docker image:

    docker run -d -p 80:80 myapp