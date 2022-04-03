# raspberry_pi_server
Raspberry PI server which takes commands from a ROS client and sends PWM commands to the connected robot arm servos.

## Install packages
In order to run the server make sure you install the required pip packages. From the root director run:

```console
foo@bar:~$ pip3 install -r ./requirements.txt
```

## Run
In order to run the server execute:

```console
foo@bar:~$ cd ./scripts
foo@bar:~$ flask run
```

## TODO - Put everything in a docker container
