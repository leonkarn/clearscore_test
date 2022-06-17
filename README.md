# clearscore_test

You need to have docker installed to run the code.
After downloading the code run the following commands:

In the directory of dockerfile
~~~
docker build . -t clearscore_image
~~~

After the image is built we run the following command to do a bind_mount without changing path
~~~
docker run -it  --mount type=bind,source="$(pwd)/main",target=/home clearscore_image /bin/bash
~~~

To produce our csv output files we just ran in the path inside the container that we are
~~~
python main_task.py
~~~

To test the functionallity of the code we run
~~~
pytest
~~~
