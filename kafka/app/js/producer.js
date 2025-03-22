const { Kafka } = require("kafkajs");

process.env.KAFKAJS_NO_PARTITIONER_WARNING = 1

const kafka = new Kafka({
    clientId: "my-producer",
    brokers: ["localhost:9092"],
});

const producer = kafka.producer();

const run = async () => {
    console.log("Connecting to producer")
    await producer.connect();
    console.log("Producer connected")

    for (let i = 0; i < 5; i++) {
        await producer.send({
            topic: "test-topic",
            messages: [{ value: `Message number ${i + 1}` }],
        });
        console.log(`✔ Message number ${i + 1} successfully sent`);
    }

    await producer.disconnect();
};

run().catch(console.error);