<p align="center">
<img src="../.github/assets/kafka.png" align="center" width="500" />
    <h1 align="center">Kafka</h1>
    <p align="center">Playground & starter</p>
</p>

# TODO

- Save topics and message in db
- k8s files
- java app example
- go app example

## Run it

```bash
docker compose up -d
```

## Quick start

### Connect to the container

```bash
docker exec --workdir /opt/kafka/bin/ -it kafka_broker sh
```

### Create a topic

```bash
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test-topic
```

and you can describe all the topics available by using

```bash
./kafka-topics.sh --describe --topic test-topic --bootstrap-server localhost:9092
```

### Write message in a topic by using the producer

```bash
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-topic
```

### Read the content of the topic

```bash
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```

## Kafka connect

```bash
echo "plugin.path=libs/connect-file-4.0.0.jar" >> config/connect-standalone.properties
```

# Application processing

Different languages or available on the `app` folder.

Each time, you much deal with a consumer and a producer.

## Consumer

He connect to the topic and retrieve each message sent to the topic.

Each consumer must be set in a consumer group, to ensure each message is proccessed by only one consumer, and not all.
This case happening generally by running consumer on multiple pods or container.

## Producer

He simply sent message to the topic.
