# distributed-tracing
Distributed tracing example in microservices architecture using flask 

## Concept
Simple example - without message broker - to demonstrate distributed tracing and logging across microservices. ServiceA requests Service B and Service C. Service C requests Service D which does a computation.

## Run the example
- `docker-compose up --build`
- Use a curl command to request Service A

e.g. `curl -v -X POST http://localhost:9000/foo`

- You will see a unique id generated with each request in the command line, copy the id
- Use the id to aggregate the logs for the specific request 

e.g. `docker-compose logs --no-color --timestamps | grep <id> | sed -e 's/^.*[|]\s//' | sort`
