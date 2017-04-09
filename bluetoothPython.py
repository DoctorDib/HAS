from bluetooth import *
import threading



def background():
    while True:
        

        nearby_devices = discover_devices(lookup_names = True)

        print "found %d devices" % len(nearby_devices)

        for name, addr in nearby_devices:
            print " %s - %s" % (addr, name)

            if name == "74:A5:28:FA:51:B7":
                print "cheese"
            else:
                print "ping"

def main():
    t = threading.Thread(target = background)
    t.start()

main()
