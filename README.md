# Loading and Performance Tests


## Technologies in use

- [Python](https://docs.python.org/3/)
- [Locust](https://docs.locust.io/)

## Prerequisites

We use [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run the loading and performance tests.   
Please install these tools from [here](https://docs.docker.com/get-docker/) before run the Locust tests.

## Getting things started locally

   Open a terminal and run this command:

      docker-compose up --scale worker=2  

    
   This will create amd start _one instance_ of **Locust** in _master_ mode and _2 workers_. 

   You can find [here](http://docs.locust.io/en/stable/running-locust-distributed.html) more details about distributed load generation in Locust.


## Running the load tests

### Running tests from the Web interface
1. Open a browser in your computer and go to : 


         http://0.0.0.0:8089/ 

2. Set the **number of users**,  **spawn rate** and fill the **tested host** (http://automationpractice.com/) and then _**Start swarming**_.

### Running tests using the `locust` command

1. Run the tests using a docker command.

   On your computer, open a terminal and run a command like:


    docker exec -it WORKER_NODE locust -f FILE_WITH_LOCUST_CLASS --headless --users 200 --spawn-rate 20 -H HTTP_SCHEMA_AND_DOMAIN  -t 10m


eq:  
 
      WORKER_NODE = load_testing_worker_1  

      FILE_WITH_LOCUST_CLASS =/mnt/locust/locustfile.py  

      HTTP_SCHEMA_AND_DOMAIN = http://automationpractice.com/


`docker exec -it load_testing_worker_1 locust -f "/mnt/locust/locustfile.py" --headless --users 100 --spawn-rate 20 -H "http://automationpractice.com/"  -t 10m`





[Here](http://docs.locust.io/en/stable/running-without-web-ui.html) are more details about running Locust tests without the web UI.