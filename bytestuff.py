def charStuff(flagbyte,escbyte,payload):
    x=payload.replace(escbyte,escbyte*2)
    y=x.replace(flagbyte,escbyte+flagbyte)
    return flagbyte+y+flagbyte
def charDestuff(flagte,escbyte,payload):
    x=payload.replace(escbyte*2,escbyte)
    y=x.replace(escbyte+flagbyte,flagbyte)
    return y[1:-1]
msg=input("enter some message:")
fb=input("enter flag byte:")
eb=input("enter escbyte:")
print("original message:",msg)
stf=charStuff(fb,eb,msg)
print("message after character stuffing:",stf)
dstf=charDestuff(fb,eb,stf)
print("message after character Destuffing:",dstf)