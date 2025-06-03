from kafka import KafkaConsumer
import json

def main():
    consumer = KafkaConsumer(
        'probando', # 'probando' es el nombre del topic a consumir
        bootstrap_servers='kafka:9092', #Dirección del servidor Kafka, en mi docker es kafka:9092
        auto_offset_reset='earliest', # Para leer desde el principio del topic (si nunca ha leido), 'latest' para leer solo nuevos mensajes
        enable_auto_commit=True, # Kafka guarda el “offset” automáticamente. El offset es un marcador que dice: “ya leí hasta aquí”.
        group_id='hrpro-consumer-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Esperando mensajes...")
    for message in consumer:
        print("Mensaje recibido:")
        print(json.dumps(message.value, indent=2))  # bonito para debug

if __name__ == "__main__":
    main()
