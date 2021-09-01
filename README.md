# flask_docker_demo_app

1. created sample flask web application which just prints the message to screen. Once hosted.
2. Hosted it using flask development server on local host at port 5001. and has been tested it on local machine.
3. Created requirements.txt and dockerfile.
4. Used below commands to build and tag the docker image 
    "docker build -f docker-file-path"
    "docker tag image-id flask-demo-app"
5. commands to run docker image with port binding: docker run -p 5001:5001 flask-app-demo    
6. tested the image on local and pushed it to git.
    git commands.
    git status
    git add .
    git commit -m 'initial code'
    git push
    
