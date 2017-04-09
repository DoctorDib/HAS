
import bluetooth
import time

target_name = "74:A5:28:FA:51:B7"
target_address = "Nexus 6P - James"

data_sent = False

while True:
    nearby_devices = bluetooth.discover_devices()
    print nearby_devices

    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break

    if (target_address is "Nexus 6P - James" ):
        print "found target bluetooth device with address ", target_address
        data_sent = True
        print "YES"
    else:
        print "could not find target bluetooth device nearby"
        data_sent = False
        print "NO"

    time.sleep(1)
