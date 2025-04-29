const { Kafka } = require("kafkajs");
const dotenv = require('dotenv')
dotenv.config()

process.env.KAFKA_GROUP_ID = "consumer-group"

const kafka = new Kafka({
    clientId: "my-consumer",
    brokers: [process.env.KAFKA_URI],
});

const consumer = kafka.consumer({ groupId: process.env.KAFKA_GROUP_ID });

const run = async () => {
    await consumer.connect();
    console.log('🔌 Consumer successfully connected')
    await consumer.subscribe({ topic: "test-topic", fromBeginning: false });

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
