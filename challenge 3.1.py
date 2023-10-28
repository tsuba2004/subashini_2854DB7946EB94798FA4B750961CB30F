def linearSearchProduct(productsList , targetProduct):
  indices=[]
  for index , product in enumerate(productsList):
    if product == targetProduct:
      indices.append(index)
      return indices



products=["shoes","boot","sandal","belt","gloves"]
target = "sandal"
result=linearSearchProduct(products,target)
print(result)
