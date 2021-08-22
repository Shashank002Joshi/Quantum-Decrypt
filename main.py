import EncryptRSA 
import DecryptRSA
import ShorBreaker

n=int(input("Enter the Bit Length "))
msg=input("Enter The Message ")
pubk,prk,ct,co=EncryptRSA.ersa(n,msg)
print("Encrypted MSG: "+ ct)
print(pubk)
print(prk)
dmt=DecryptRSA.drsa(co,prk)
print("\nDecrypted Msg: "+ dmt)
dmts=ShorBreaker.sbreak(co,pubk)
print("\nDecrypted Msg (Using Shor Algorithm): "+dmts)

