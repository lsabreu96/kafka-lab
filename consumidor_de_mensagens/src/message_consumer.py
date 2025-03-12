# Adaptado de https://github.com/confluentinc/confluent-kafka-python
from confluent_kafka import Consumer
import os
import logging

logging.basicConfig(level=logging.INFO)
consumer_config = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVER'),
    'group.id': os.getenv('KAFKA_CONSUMER_GROUP_ID'),
    'auto.offset.reset': 'earliest'
}

topico = os.getenv('KAFKA_CONSUMER_TOPICS')

consumidor = Consumer(**consumer_config)
consumidor.subscribe([topico])

logging.debug(f"Consumidor iniciado para o tópico: {topico}")

def consome_mensagens():
    while True:
        msg = consumidor.poll(1.0)  # Timeout ajustado

        if msg is None:
            logging.debug("Nenhuma mensagem recebida...")
            continue

        if msg.error():
            logging.error(f"Erro no consumo: {msg.error()}")
            continue

        logging.info(f"Mensagem recebida: {msg.value().decode('utf-8')}")

if __name__ == "__main__":
    consome_mensagens()

