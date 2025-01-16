Producer: Entidade que produz mensagens e as envia pro Kafka

Consumer: entidade que lê mensagens e as envia pro Kafka

Broker: é o nome dado pro servidor Kafka. Recebe esse nome (broker é traduzido como intermediário) por intermediar a comunicação entre produtores e consumidores

Tópicos: conjunto lógica que agrega mensagens de vários produtores que tem um contexto parecido. Pode ser pensado como se fosse uma tabela de um banco de dados

Partição de um tópico: estratégia de dividir os dados de um dado tópico entre múltiplas máquinas

Offset de uma partição: identificador de uma mensagem. São restritos a partição e não são globalmente acordados.

Consumer group: Grupo de consumiodres de um dado tópico. Cada entidade do consumer group pode mais de uma partiçaõ de um tópico até o ponto de que o número de consumidores fique igual ao e partiçoes. É o membro que escala nums sistema Kafka. Não se pode ter mais de um consumidor (no grupo) para um mesmo tópico p evitar leitura duplicada

Kafka Connect: middleware que faz a interface entre um produtor/consumidor e o Kafka. Exemplos: Source Kafka Connect (puxa de um banco de dados e escreve no Kafka) e Sink Kafka Connect (puxa do Kafka e escreve em algum lugar).
Source e Sink podem ser escritos no mesmo Cluster
Todo connect tem um connector e um task, o connector gera as tasks e passa para o task que então entregam os dados pro connect p mandar pro kafka



ZooKeeper: opera como um sistema de coordenação entre os brokers Kakfa, que será deprecado.


# Parâmetros mínimos necessários pro 