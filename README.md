# kafka

Each container is given individual hostanme and portname, otherwise *Kafdrop* cannot connect to the container and throws error.


### Enviroment Variables

1. **KAFKA_BROKER_ID**: This parameter sets the unique ID for the Kafka broker in a Kafka cluster. It should be a unique integer value for each broker in the cluster.

2. **KAFKA_INTER_BROKER_LISTENER_NAME**: This parameter sets the name of the listener used for communication between Kafka brokers in a cluster. In this case, it's set to INTERNAL, which matches the listener name used in *KAFKA_LISTENERS* and *KAFKA_ADVERTISED_LISTENERS*

3. **KAFKA_LISTENER_SECURITY_PROTOCOL_MAP**: It maps security protocols to listeners. In this configuration, it specifies that the *INTERNAL* listener uses the *PLAINTEXT* security protocol.

4. **KAFKA_ZOOKEEPER_CONNECT**: It specifies the Zookeeper connection string that the Kafka broker uses to connect to the Zookeeper ensemble. In this case, it's set to *zookeeper:2181*.

5. **KAFKA_ADVERTISED_HOST_NAME**: This parameter defines the hostname or IP address that the Kafka broker advertises to clients for connecting to it. Here, it's set to *broker1, broker2, broker3*.

6. **KAFKA_ADVERTISED_PORT**: It specifies the port that the Kafka broker advertises to clients for connecting to it. In this case, it's set to *9092:9094*.

7. **KAFKA_LISTENERS**: This parameter defines the listeners that the Kafka broker uses to accept incoming connections. In this configuration, it specifies a listener named INTERNAL with the address *kafka:9092*. Syntax is *<Protocol://Host:Port>*.

8. **KAFKA_ADVERTISED_LISTENERS**: This parameter defines the listeners that the Kafka broker advertises to clients. In this case, it advertises the INTERNAL listener at *kafka:9092*. Syntax is *<Protocol://Host:Port>*.
