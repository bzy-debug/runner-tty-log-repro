FROM busybox:1.36

RUN for i in 1 2 3 4 5; do echo "docker build layer $i"; sleep 1; done
