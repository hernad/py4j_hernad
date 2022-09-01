import os
import subprocess
import sys
import threading
from time import sleep
from py4j.java_gateway import JavaGateway, CallbackServerParameters

print("start py4j gateway ...")
global proc1

#class ThreadWithTrace(threading.Thread):
#  def __init__(self, *args, **keywords):
#    threading.Thread.__init__(self, *args, **keywords)
#    self.killed = False
# 
#  def start(self):
#    self.__run_backup = self.run
#    self.run = self.__run     
#    threading.Thread.start(self)
# 
#  def __run(self):
#    sys.settrace(self.globaltrace)
#    self.__run_backup()
#    self.run = self.__run_backup
# 
#  def globaltrace(self, frame, event, arg):
#    if event == 'call':
#      return self.localtrace
#    else:
#      return None
# 
#  def localtrace(self, frame, event, arg):
#    if self.killed:
#      if event == 'line':
#        raise SystemExit()
#    return self.localtrace
# 
#  def kill(self):
#    self.killed = True

cmd_java = ["java","-jar", "C:/Users/ernad.husremovic.SA/dev/ziher_mono/py4j/target/py4j-hernad-1.0-SNAPSHOT.jar"]


def output_reader(proc, file):
    while True:
        byte = proc.stdout.read(1)
        if byte:
            sys.stdout.buffer.write(byte)
            sys.stdout.flush()
            file.buffer.write(byte)
        else:
            break

def proc2():
    print("dalje ....")
    #sleep(1)
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
    gw.close()
    print("java gateway closed")

    sleep(9)
    print("nakon sleep 10 ubij proc1")
    proc1.kill()
    print("============ end =================")
    sys.exit()

with subprocess.Popen(cmd_java, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc1, open('javagw.log', 'w') as javalogfile:
    global java_thread 
    java_thread = threading.Thread(target=output_reader, args=(proc1, javalogfile))
    t2 = threading.Thread(target=proc2, args=())
    java_thread.start()
    t2.start()
    java_thread.join()
    t2.join()


