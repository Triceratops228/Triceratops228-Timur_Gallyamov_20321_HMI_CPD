# Задание:

Разобрать пример Python с GitHub.
В github пример Python. С добавленным сервисом и полями, которые используются.

# Результат:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/2feb9df6-33da-4efb-b6d8-4b38a76f7dff)

# Пояснение:

Указываем количество телефонов, название и цену каждого. Добавил новую функцию удаления телефона из списка телефонов и дополнил функцию getProduct теперь она выводит список телефонов

# Листинг:

# Серверная часть:

``` py
from concurrent import futures
import logging
import uuid
import grpc
import time

import product_info_pb2
import product_info_pb2_grpc

class ProductInfoServicer(product_info_pb2_grpc.ProductInfoServicer):

    def __init__(self):
        self.productMap = {}

    def addProduct(self, request, context):
        id = uuid.uuid1()
        request.id = str(id)
        print("addProduct:request", request)
        self.productMap[str(id)] = request
        response = product_info_pb2.ProductID(value = str(id))
        
        print("addProduct:response", response)
        return response

    def getProduct(self, request, context):
        #print("getProduct:request", request)
        id = request.value
        response = self.productMap[str(id)]
        #print("getProduct:response", response)
        return response
    def delProduct(self,request,context):
        id = request.value
        response = self.productMap.pop(str(id))
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
product_info_pb2_grpc.add_ProductInfoServicer_to_server(
        ProductInfoServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
```

# Клиентская часть:

``` py
import grpc
import product_info_pb2
import product_info_pb2_grpc
import random
import time;

names=[]
def run():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = product_info_pb2_grpc.ProductInfoStub(channel)
    for i in range(int(input("Сколько телефонов:"))):
        response = stub.addProduct(product_info_pb2.Product(name = str(input("Название телефонов:")), description = "Brand new Phone", price = int(input("Цена:")) ))
        names.append(response.value)
    #print("add product: response", response)
    #productInfo = stub.getProduct(product_info_pb2.ProductID(value = response.value))
    #print("get product: response", productInfo)
    choice=random.choice(names)
    stub.delProduct(product_info_pb2.ProductID(value = choice))
    names.remove(choice)
    print("All Phones:")
    for i in names:
        List = stub.getProduct(product_info_pb2.ProductID(value = i))
        print(List)

run()
```

# Прото файл:

``` py
syntax = "proto3";

package ecommerce;

service ProductInfo {
    rpc addProduct(Product) returns (ProductID);
    rpc getProduct(ProductID) returns (Product);
    rpc delProduct(ProductID) returns(Product);
}

message Product {
    string id = 1;
    string name = 2;
    string description = 3;
    float price = 4;
}

message ProductID {
    string value = 1;
}
```
