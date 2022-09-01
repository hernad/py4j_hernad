from py4j.java_gateway import JavaGateway, CallbackServerParameters
gw = JavaGateway()
java_list = gw.jvm.java.util.ArrayList()
java_list.append(100)
java_list.append(200)

java_list_2 = gw.jvm.java.util.ArrayList()
java_list_2.append(300)
java_list_2.append(400)

print("java list:", java_list)
print("java_list 2:", java_list_2)


print("java version", gw.jvm.System.getProperty("java.runtime.version"))
