package main

import (
	"fmt"
	"log"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {
	c, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": "localhost:9092",
		"group.id":          "test-group",
		"auto.offset.reset": "earliest",
	})
	if err != nil {
		log.Fatalf("Error while creating the consumer: %v\n", err)
	}
	defer c.Close()

	topic := "test-topic"
	err = c.SubscribeTopics([]string{topic}, nil)
	if err != nil {
		log.Fatalf("Error while connecting to topic: %v\n", err)
	}

	fmt.Println("Successfully connected to the topic, waiting for message...")

	for {
		msg, err := c.ReadMessage(-1)
		if err == nil {
			fmt.Printf("Message received: %s\n", string(msg.Value))
		} else {
			log.Printf("Error while reading the message: %v\n", err)
		}
	}
}
