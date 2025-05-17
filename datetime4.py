import datetime as ts,time,os
tarih= ts.datetime.now()

while True:
      
      os.system('cls')
      tarih= ts.datetime.now()
      print(tarih.strftime(">>>%H:%M:%S <<<"))
      time.sleep(1)
      os.system('cls')


