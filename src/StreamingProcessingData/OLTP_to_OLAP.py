from OLTP_Producer import OLTPProducer
from OLTP_Consumer import OLTPConsumer
import time

if __name__ == '__main__':
  opt = int(input('1 - Producer \n2 - Consumer: '))
  if opt == 1:
    while True:
      oltpProducer = OLTPProducer('oltp')
      time.sleep(0.5)
      oltpProducer.DumpData
  elif opt == 2:
    while True:
      oltpConsumer = OLTPConsumer('oltp')
      time.sleep(0.5)
      oltpConsumer.ConsumerOLTP