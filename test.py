from ctypes import sizeof
import pyDH
import time
from queue import Queue
from threading import Thread
import communication
from IpSec import IpSec, Messeng, IKE2
import copy
import pickle



def serwer(quote): 

    srv = communication.Server('localhost',quote)

    srv.start()

    

    

def client(quote,messeng):

    communication.Client.sendMesseng('localhost',messeng)










if __name__ == "__main__":

    d1 = IKE2()
    d2 = IKE2()
    d1_pubkey = d1.generatePublicKey()
    d2_pubkey = d2.generatePublicKey()
    print("d1_pubkey = " , d1_pubkey, " || d2_pubkey = ", d2_pubkey)
    d1_sharedkey = d1.generatePrivateKey(d2_pubkey)
    d2_sharedkey = d2.generatePrivateKey(d1_pubkey)
    print("d1_sharedkey = " , d1_sharedkey, " || d2_sharedkey = ", d2_sharedkey, "type = ", type(d1_sharedkey))

    print(d1_sharedkey == d2_sharedkey)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # q = Queue()

    # t1 = Thread(target = serwer, args =(q,))

    # #t2 = Thread(target = client, args =(q,messeng))

    # t1.start()

    # #t2.start()

    # counter = 1

    # while True:

    #     print('d')

       

    #     data = 'Zaszyfrowana wiadomosc numer ' + str(counter)

    #     counter+=1

    #     pakiet = IpSec(data ,'127.0.0.1')

    #     pakiet.encryptdata(None)



    #     #sa = SecurityAssociation(ESP, spi=0xdeadbeef, crypt_algo='AES-CBC', crypt_key=b'-\xbd\xb6Q\xa6\x7f6c\x08\xb7\x0coU\xcfg\xcd')

   
    #     time.sleep(3)
    #     communication.Client.sendMesseng('127.0.0.1',pakiet.toBytes())

     

    #     odczyatana  = IpSec.fromBytes(q.get())

    #     print("Wiadomosc  odczyatana",odczyatana.data)





    #     odszyfrowana = odczyatana.decryptdata(None)

    #     print("Wiadomosc  odszyfrowana",type(odszyfrowana.data))

    #     print("Wiadomosc  odszyfrowana",odszyfrowana.data)



        #zawartosc = Messeng.fromBytes(odszyfrowana.data)ps -a


        

        #print("Wiadomosc   zawartosc", Messeng.fromBytes(odszyfrowana.data) )



    

    #print('Server posiada w buforze', srv.msgBuffor)

    #print(p1.stdout)
