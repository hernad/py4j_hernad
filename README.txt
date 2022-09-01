C:\Users\ernad.husremovic.SA>python
Python 3.11.0rc1 (main, Aug  8 2022, 11:30:54) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.


>>> from py4j.java_gateway import JavaGateway, CallbackServerParameters
>>> gateway = JavaGateway()
>>> java_list = gateway.jvm.java.util.ArrayList()
>>> java_list.append(100)
>>> java_list.append(200)
>>> java_list
[100, 200]
>>> java_list.append(50)
>>> java_list
[100, 200, 50]
>>> gateway.jvm.java.util.Collections.sort(java_list)
>>> java_list
[50, 100, 200]


## OpenJDK microsoft build

https://docs.microsoft.com/en-us/java/openjdk/download
