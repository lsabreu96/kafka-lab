# Adaptado de https://github.com/confluentinc/confluent-kafka-python
from confluent_kafka import Consumer
import os
import logging


logging.basicConfig(level=logging.INFO)
consumer_config = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVER'),
    'group.id': os.getenv('KAFKA_CONSUMER_GROUP_ID'),
    'auto.offset.reset': os.getenv('KAFKA_OFFSET_RESET')
}

topico = os.getenv('KAFKA_CONSUMER_TOPICS')

consumidor = Consumer(**consumer_config)
consumidor.subscribe([topico])

logging.debug(f"Consumidor iniciado para o tópico: {topico}")

clientes = []

class Cliente:
    _instancias = []

    def __init__(self, nome:str, saldo:float=0):
        self.nome = nome
        self.debitos = []
        self.creditos = []
        Cliente._instancias.append(self)


    @classmethod
    def cria_ou_recupera_cliente(cls, nome:str):
        for instancia in cls._instancias:
            if instancia.nome == nome:
                return instancia
 
        logging.info(f"Criando usuario {nome}")        
        return cls(nome)


    def processa_entrada(self, valor: float, operacao: str):
        if operacao == 'D':
            self.debitos.append(float(valor))
        
        if operacao == 'C':
            self.creditos.append(float(valor))

        logging.info(f"Saldo atual do usuário é de {self.processa_saldo()}")


    def processa_saldo(self)->float:
        return sum(self.creditos) + sum(self.debitos)


def processa_clientes():
    while True:
        msg = consumidor.poll(1.0)
    
        if msg is None:
            logging.debug("Nenhuma mensagem recebida...")
            continue

        if msg.error():
            logging.error(f"Erro no consumo: {msg.error()}")
            continue
        
        hora, usuario, valor, operacao = msg.value().decode('utf-8').split('<>')
        cliente = Cliente.cria_ou_recupera_cliente(usuario)
        cliente.processa_entrada(valor, operacao)


        logging.info(f"Mensagem recebida: {msg.value().decode('utf-8')}")


if __name__ == "__main__":
    processa_clientes()

