import pika
import sys
import os
import django
import simplejson as json
# from apps.pipeline.one_c.rmq.utils import create_product, update_product, stock_product, change_order_status


def main():
    host = 'rabbitmq-univer'
    # host = '185.125.44.186'
    credentials = pika.PlainCredentials('user', 'user')
    parameters = pika.ConnectionParameters(host, 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel_updated = connection.channel()
    channel_stocks = connection.channel()
    channel_order_status = connection.channel()

    channel.queue_declare(queue='updated_product_queue')
    channel_updated.queue_declare(queue="new_product_queue")
    channel_stocks.queue_declare(queue="product_store_count_queue")
    channel_order_status.queue_declare(queue="order_changes_status")

    def callback(ch, method, properties, body):
        updated_product = json.loads(body)
        # update_product(updated_product)

    def product_count(ch, method, properties, body):
        print('product count saving')
        stocks_product = json.loads(body)
        # stock_product(stocks_product)

    def new_product_callback(ch, method, properties, body):
        new_product = json.loads(body)
        # print('new_product')
        # create_product(new_product)

    def order_status_change(ch, method, properties, body):
        order = json.loads(body)
        # print('new_product')
        # change_order_status(order)

    channel_updated.basic_consume(queue='updated_product_queue', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='new_product_queue', on_message_callback=new_product_callback, auto_ack=True)
    channel_stocks.basic_consume(queue='product_store_count_queue', on_message_callback=product_count, auto_ack=True)
    channel_order_status.basic_consume(queue="order_changes_status", on_message_callback=order_status_change, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    channel_updated.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)