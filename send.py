import pika
import json
import constant


def sendRabbitMQ(body):
    credentials = pika.PlainCredentials('rabbit', 'rabbitpass')
    paramaters = pika.ConnectionParameters(host='localhost',
                                           port=5672,
                                           virtual_host='dev',
                                           credentials=credentials,
                                           socket_timeout=10,
                                           connection_attempts=100,
                                           heartbeat=30)

    parameters = pika.URLParameters(
        'amqp://rabbit:rabbitpass@localhost:5672/dev?socket_timeout=10&connection_attempts=100&heartbeat=30'
    )

    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hieuQueue',
                          durable=True,
                          exclusive=False,
                          auto_delete=False)

    channel.confirm_delivery()

    try:
        channel.basic_publish(exchange='amq.topic',
                              routing_key='update.info.gateway.hieuTest',
                              body=json.dumps(body),
                              properties=pika.BasicProperties(
                                  content_type='text/plain', delivery_mode=1),
                              mandatory=True)
    except pika.exceptions.UnroutableError as e:
        print('Unroutable')
        print(e)
    except Exception as e:
        print(e)

    connection.close()


def byte2str(inputByte):
    string = inputByte.decode('utf-8')
    return string


def str2byte(inputString):
    data = inputString.encode('utf-8')
    return data


class ReceiveMonitor():
    def __init__(self, msgType, status, msg, routingKey):
        self.msgType = msgType
        self.status = status
        self.msg = msg
        self.routingKey = routingKey

    def getJSON(self):
        return {
            "type": constant.ANSWER_TYPE,
            "payload": {
                "type": self.type,
                "status": self.status,
                "msg": self.msg
            },
            "routingKey": self.routingKey
            # "monitor.result.cli_93f70840-719e-4a79-bf74-e51a6e1c9708"
        }


constant.ANSWER_PAYLOAD_STATUS.get('SUCCESS')