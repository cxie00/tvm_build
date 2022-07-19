# tvm_build
This builds a Docker container with TVM.

Steps to build the image:
1. Install docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 
2. Clone this repo 
3. Build the docker image:
```vi Dockerfile
docker build -t tvm_build:1 . 
docker run -it tvm_build:1 /bin/bash
```
<p>
Docker image general usage: 
```vi Dockerfile      // to edit the Dockerfile
docker build -t <name>:<tag> [-f Dockerfile] .    // to build the Dockerfile. <> is required and [] is optional
docker run -it <name>:<tag> /bin/bash       // to run the Dockerfile. Keep the Dockerfile in the same folder as the other things
```
