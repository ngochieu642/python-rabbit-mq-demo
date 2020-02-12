import pika
import json
from dotmap import DotMap

from constant import AGENT_MONITOR
AGENT_MONITOR = DotMap(AGENT_MONITOR)


def sendRabbitMQ(body):
    '''
    This function receive a dict-like body and send them to queue
    '''
    # credentials = pika.PlainCredentials('rabbit', 'rabbitpass')
    # paramaters = pika.ConnectionParameters(host='localhost',
    #                                        port=5672,
    #                                        virtual_host='dev',
    #                                        credentials=credentials,
    #                                        socket_timeout=10,
    #                                        connection_attempts=100,
    #                                        heartbeat=30)

    parameters = pika.URLParameters(
        'amqp://rabbit:rabbitpass@localhost:5672/monitor?socket_timeout=10&connection_attempts=100&heartbeat=30'
    )

    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hieuQueue',
                          durable=True,
                          exclusive=False,
                          auto_delete=False)

    channel.confirm_delivery()

    try:
        channel.basic_publish(
            exchange='amq.topic',
            routing_key='monitor.update.cli_10041997',
            # routing_key='update.info.gateway.cli_10041997',
            body=json.dumps(body),
            properties=pika.BasicProperties(content_type='text/plain',
                                            delivery_mode=1),
            mandatory=True)
    except pika.exceptions.UnroutableError as e:
        print('UnRoutable')
        print(e)
    except Exception as e:
        print(e)

    connection.close()


class ReceiveMonitor():
    def __init__(self, payloadType, status, msg, routingKey, container_type,
                 before_version, current_version):
        self.payloadType = payloadType
        self.status = status
        self.msg = msg
        self.routingKey = routingKey
        self.container_type = container_type
        self.before_version = before_version
        self.current_version = current_version

    def getDict(self):
        return {
            "type": AGENT_MONITOR.TYPE.ANSWER,
            "payload": {
                "type": self.payloadType,
                "status": self.status,
                "msg": self.msg,
                "container_type": self.container_type,
                "before_version": self.before_version,
                "current_version": self.current_version
            },
            "routingKey": self.routingKey
        }


for i in range(1):
    testAnswer = ReceiveMonitor(
        payloadType=AGENT_MONITOR.ANSWER.PAYLOAD.TYPE.UPDATE,
        status=AGENT_MONITOR.ANSWER.PAYLOAD.STATUS.SUCCESS,
        msg="Updated by Hieu on day %d" % (i),
        container_type="db",
        before_version="1.0",
        current_version="1.1",
        routingKey="monitor.update.cli_93f70840-719e-4a79-bf74-e51a6e1c9708")

    sendRabbitMQ(testAnswer.getDict())