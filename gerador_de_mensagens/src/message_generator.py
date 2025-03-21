# Adaptado de https://github.com/confluentinc/confluent-kafka-python
import time
from faker import Faker
from datetime import datetime
import random
from confluent_kafka import Producer
import os


# Inicializar o Faker
fake = Faker()
produtor = Producer({'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVER')})

usuarios = ['João', 'Maria', 'José']

def gerar_saida():
    while True:
        hora_atual = datetime.now().strftime("%H:%M:%S")

        usuario  = random.choice(usuarios)
        
        valor = round(random.uniform(1.0, 100.0), 2)

        tipo = random.choice(['C', 'D'])
        
        produtor.produce(
            os.getenv('KAFKA_TOPIC'),
            f"{hora_atual}<>{usuario}<>{valor}<>{tipo}".encode('utf-8')
        )
        
        time.sleep(1)

if __name__ == "__main__":
    gerar_saida()
