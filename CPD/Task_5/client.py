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