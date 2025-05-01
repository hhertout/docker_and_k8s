const amqp = require('amqplib');
const dotenv = require('dotenv')

dotenv.config()

const { MQ_ENDPOINT, MQ_USER, MQ_PASSWORD } = process.env

const RABBITMQ_URL = `amqp://${MQ_USER}:${MQ_PASSWORD}@${MQ_ENDPOINT}`

async function testRabbitMQ() {
    try {
        const connection = await amqp.connect(RABBITMQ_URL);
        console.log('Connected to RabbitMQ');

        const channel = await connection.createChannel();
        console.log('Channel created');

        const queue = 'testQueue';
        await channel.assertQueue(queue, { durable: false });
        console.log(`Queue '${queue}' is ready`);

        channel.sendToQueue(queue, Buffer.from('Hello RabbitMQ!'));
        console.log(`Message sent to queue '${queue}'`);

        channel.consume(queue, (msg) => {
            console.log(`Received message: ${msg.content.toString()}`);
            channel.ack(msg);
        });

    } catch (error) {
        console.error('Error connecting to RabbitMQ:', error);
    }
}

testRabbitMQ();
