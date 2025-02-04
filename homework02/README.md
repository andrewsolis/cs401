# homework 02 guide

## to build images from dockerfiles, run:

### - docker build -t homework02-writer -f Dockerfile.writer . (for writer)
### - docker build -t homework02-computer -f Dockerfile.computer . (for computer)
### - docker build -t homework02-html -f Dockerfile.html  . (for htmls)

## to run without docker compose, do these:

### - docker run -v $PWD/data:/data/ homework02-writer (for writer.py) 
### - docker run -v $PWD/data:/data/ homework02-computer (for computer.py) 
### - docker run -d -p 8000:8000 -v $PWD/data:/data homework02-html (for htmls)

## to build/run with docker compose:

### - check if port in use with:
#### docker container ls
### if anything comes up, copy the <ID>, and run:
#### docker stop <ID>
### Once port is free, run:
#### docker-compose up --build
### then run:
####  docker-compose up
### ...this will activate all services in the docker compose file, writer, computer, and the html files.
 
