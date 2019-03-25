---
layout: post
title:  "Kafka Quickstart"
date:   2019-03-25-kafka/2019-03-25
desc: "Quick test on writing code snippets in a blog post"
keywords: "Kafka"
categories: [Kafka]
tags: [JS,Jekyll]
icon: icon-html
---

## Kafka Quickstart



### Zookeeper, java가 설치되어 있는 Host에서 시작
   
1. Zookeeper 서버 시작
   >sh zookeeper-server-start.sh ../config/zookeeper.properties

![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-26-30.png){: .wh60 .center}

3. Kafka 서버 시작
   >bin/kafka-server-start.sh config/server.properties

![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-27-03.png){: .wh60 .center}

4. Topic 생성 및 리스트 확인
   >bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partition 1 --topic js_test1

   >bin/kafka-topics.sh --list --zookeeper localhost:2181

![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-27-48.png){: .wh65 .center}

5. Producer 시작
   >bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-28-29.png){: .wh60 .center}

6. Consumer 시작
   >bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-28-55.png){: .wh60 .center}

7. Multi-broker-cluster 설정
   
   기존의 내용을 복사
   >cp server.properties server-1.properties
   >cp server.properties server-2.properties

   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-29-45.png){: .wh60 .center}

   내용을 변경한다.
   ( broker.id=1 / listeners=PLAINTEXT://:9093 / log.dirs=/tmp/kafka-logs-1 )

   >vi server-1.properties

   broker.id=1
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-30-31.png){: .wh60 .center}

   listeners=PLAINTEXT://:9093
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-30-53.png){: .wh60 .center}

   log.dirs=/tmp/kafka-logs-1
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-31-08.png){: .wh60 .center}

   >vi server-2.properties

   broker.id=2
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-31-38.png){: .wh60 .center}

   listeners=PLAINTEXT://:9094
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-31-54.png){: .wh60 .center}

   log.dirs=/tmp/kafka-logs-2
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-32-09.png){: .wh60 .center}

8. 두 개의 새로운 노드 시작
   
   >bin/kafka-server-start.sh config/server-1.properties &
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-32-35.png){: .wh60 .center}

   마지막 로그에서 kafkaserver id=1 가 started 되었다는 것을 확인 할 수 있습니다.
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-32-50.png){: .wh60 .center}

   bin/kafka-server-start.sh config/server-2.properties &
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-33-03.png){: .wh60 .center}

   마지막 로그에서 kafkaserver id=2 가 started 되었다는 것을 확인 할 수 있습니다.
   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-33-16.png){: .wh60 .center}

   ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-33-26.png){: .wh55 .center}

9. replication-factor 3인 것으로 topic을 새로 생성

    >bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partition 1 --topic my-replicated-topic

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-33-57.png){: .wh65 .center}

10. 브로커가 무엇을 하고 있는지 확인

    >bin/kafka-topic.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-34-30.png){: .wh60 .center}

    • "Leader"는 주어진 파티션에 대한 모든 읽기 및 쓰기를 담당하는 노드입니다. 각 노드는 임의로 선택된 파티션 부분의 리더가됩니다.

    • "Replicas"은 리더인지 또는 현재 살아 있는지 여부에 관계없이이 파티션의 로그를 복제하는 노드 목록입니다.

    • "Isr"은 "동기화 된"복제본 집합입니다. 이것은 현재 살아 있고 리더에게 포착 된 복제본 목록의 하위 집합입니다.

    처음에 생성했던 topic을 확인
    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-35-52.png){: .wh60 .center}

11. 새로 만들었던 topic에 메시지 내용을 추가
    
    >bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-replicated-topic

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-36-22.png){: .wh60 .center}

    >bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-replicated-topic --from-beginning

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-36-47.png){: .wh60 .center}

12. Fault-Tolerance TEST
    Broker 1의 프로세스를 제거 후, 변화 상황을 테스트 진행

    프로세스 ID 확인
    >ps aux \| grep server-1.properties

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-37-36.png){: .wh60 .center}

    프로세스 ID = 8657을 제거
    >kill -9 8657

    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-37-58.png){: .wh60 .center}

    Consumer console에서 변경사항에 대한 내용을 확인 할 수 있다.
    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-38-12.png){: .wh60 .center}

    Broker 1이 죽은 시점에서 "Isr"의 1이 사라진 것을 확인 할 수 있다.
    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-38-24.png){: .wh60 .center}

    Broker 1이 죽어도 Broker 2로 Fault-Toleranse가 되었기때문에 메시지 전송에는 이상이 없는 것을 확인 가능하다.

    **[producer-console]**
    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-38-59.png){: .wh60 .center}

    **[consumer-console]**
    ![](/static/assets/img/blog/2019-03-25-kafka-quickstart/2019-03-25-20-39-24.png){: .wh60 .center}
