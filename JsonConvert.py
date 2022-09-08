
import json

file_text={ "name":"john", "age":22, "sex":"man", "address":"USA" }

#字典
print(file_text)
print(type(file_text))
# json 转字符串
print(json.dumps(file_text))
print(type(json.dumps(file_text)))