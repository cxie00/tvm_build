# tvm_build

vi Dockerfile      // to edit the Dockerfile
 
docker build -t <name>:<tag> [-f Dockerfile] .    // to build the Dockerfile
 <> is required and [] is otional

docker run -it <name>:<tag> /bin/bash       // to run the Dockerfile. Keep the Dockerfile in the same folder as the other things


Examples:

vi Dockerfile
docker build -t tvm_build:2 . 
docker run -it tvm_build:2 /bin/bash 
