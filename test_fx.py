from py4j.java_gateway import JavaGateway, CallbackServerParameters
gw = JavaGateway()

java_list = gw.jvm.java.util.ArrayList()
java_list.append(300)
java_list.append(400)

print("java list:", java_list)
print("java version", gw.jvm.System.getProperty("java.runtime.version"))

try:
  gw.entry_point.getStack()
except: 
  print("java fx vec pokrenut")
gw.entry_point.getStack2()
gw.entry_point.getStack2()