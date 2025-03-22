const { Kafka } = require("kafkajs");

process.env.KAFKA_GROUP_ID = "consumer-group"

const kafka = new Kafka({
    clientId: "my-consumer",
    brokers: ["localhost:9092"],
});

const consumer = kafka.consumer({ groupId: process.env.KAFKA_GROUP_ID });

const run = async () => {
    await consumer.connect();
    console.log('🔌 Consumer successfully connected')
    await consumer.subscribe({ topic: "test-topic", fromBeginning: true });

    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            console.log({
                topic: topic,
                key: message.key?.toString(),
                value: message.value?.toString(),
                partition: partition,
                headers: message.headers,
            })
        },
    });
};

run().catch(console.error);
