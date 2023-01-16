## Set up

There are two ways to run this project:

### Local environment
```bash
cd app
pip3 install -r requirements.txt
flask --app main run

# unit test
pytest

# curl test
curl --location --request POST 'http://127.0.0.1:8080' \
--header 'Content-Type: application/json' \
--data-raw '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
'
```

### Docker
```bash
# on Compose V2, the new docker compose command was introduced; if you are using an older version, use docker-compose instead
docker compose up -d

# enter the container
docker exec -it delivery_fee_calculator-app-1 bash

# destroy
docker compose down

```

## Reflections

If the delivery fee calculator is a part of a larger system as a miroservice, I would consider the following:

1. Use a message queue to decouple the delivery fee calculator from the rest of the system. Because this service maybe down for a while of be called by a large number of users simultaneously. If we use message queue, the delivery fee calculator can be scaled independently from the rest of the system. 

2. Deploy a load balancer to distribute the load to multiple instances of the delivery fee calculator if there are numerous calls to the service.

3. Implement observability to monitor the health of the service and the performance of the service.

4. Log the requests and responses to the service into files to help with debugging.