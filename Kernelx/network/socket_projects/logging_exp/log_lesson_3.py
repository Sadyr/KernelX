import logging
logging.basicConfig(filename='admin.log', filemode='a',format='%(asctime)s - %(message)s ', level=logging.INFO)
logging.info('Admin logged in')
