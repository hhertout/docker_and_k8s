package main

import (
	"fmt"
	"log"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {
	p, err := kafka.NewProducer(&kafka.ConfigMap{
		"bootstrap.servers": "localhost:9092",
	})
	if err != nil {
		log.Fatalf("Error while creating the Producer: %v\n", err)
	}
	defer p.Close()

	topic := "test-topic"

	msg := "Hello Kafka from Go!"
	err = p.Produce(&kafka.Message{
		TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
		Value:          []byte(msg),
	}, nil)

	if err != nil {
		log.Fatalf("Error while creating message: %v\n", err)
	}

	e := <-p.Events()
	m, ok := e.(*kafka.Message)
	if ok && m.TopicPartition.Error != nil {
		log.Fatalf("Error while sending message: %v\n", m.TopicPartition.Error)
	}

	fmt.Println("Message successfully sent !")
}
