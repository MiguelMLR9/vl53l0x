from vl53l0x import setup_tofls_same_bus
from machine import Pin
i2cID=1
sda=14
scl=15
#example with 3 tofls (have to be 2 or more)
#tofls xshut pins
tofl0_xshut=None #first tofl of i2c always is None (xshut pin NOT wired)
tofl1_xshut=16
tofl2_xshut=17
#add all xshut pins to a list (have to be ordered: tofl0,tofl1,tofl2,...)
tofls_xshut=[tofl0_xshut,tofl1_xshut,tofl2_xshut]
#call setup_tofls_same_bus func, will return a list with tofl objects                   
tofls=setup_tofls_same_bus(tofls_xshut,i2cID,sda,scl)
try:
    while True:
        values=[]
        data=""
        #call ping in each tofl to know distance, save on a list,
        #and print values
        for i in range(len(tofls)):
            values.append(tofls[i].ping())
            data+="s"+str(i)+": "+str(values[i])+" mm.\t"
        print(data)
finally:
    # Restore default address and xshut pin.
    # Have to restore ALL tofl from EACH i2c:
    # if are using 2 i2c: modify the code below to restore 
    # address and xshut pin from second i2c too
    print("Restoring")
    for i in range (len(tofls)):
        tofls[i].set_address(0x29)
        if i>0:
            #xshut pin as Pin.OUT
            device_xshut=Pin(tofls_xshut[i],Pin.OUT)
            #disable xshut pin (low)
            device_xshut.value(0)
        print("tofl",i,"done")




