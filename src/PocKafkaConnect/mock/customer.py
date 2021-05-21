from datetime import datetime

from faker import Faker

class CustomerDataProducer:
  
  def __init__(self):
    self.__fake = Faker()
    self.__customer_name = self.__fake.name()
    self.__customer_address = self.__fake.address().replace('\n', ' - ')
    self.__customer_buy_price = self.__fake.pricetag()
    self.__createdAt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
  @property
  def generateCustomer(self):
    customer = {'customer_name':self.__customer_name, \
        'customer_address': self.__customer_address, \
        'customer_buy_price': self.__customer_buy_price, \
        'createdAt': self.__createdAt}
    
    return customer