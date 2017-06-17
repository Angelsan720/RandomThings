#! /usr/bin/env python2

"""
Yeah I'm lazy
Having to plug in a cable into my hpone to transfer junk like music got frustrating
So I whipped this up to use Pushbullet to send things to my phone or browser
Might adjust it to use another app depending if pushbullet doesnt work out long term
"""
"""
Note this only partially works in python 3
It works fine in python 2
"""

from pushbullet import Pushbullet
import sys
import ConfigParser
import os
def Usage():
        print("Usage: %s [file to upload 1] <file to upload 2> <file upload 3...>")
        sys.exit(0)
def run():
        Config = ConfigParser.ConfigParser()
        n = len(os.path.basename(__file__))
        Config.read("%s/config"%(sys.argv[0][0:-n]))
        TOKEN = Config.get("Pushbullet" , "Token")
        pb = Pushbullet(TOKEN)

        print("getting devices:")
        d = -1
        while d not in range(0 , len(pb.devices)):
                for i in range(0 , len(pb.devices)):
                        print(i , pb.devices[i])
                try:
                        d = int(raw_input("\nselect a device:"))
                except:
                        pass
        phone = pb.devices[d]

        for i in range(1 , len(sys.argv)):
                f = open(sys.argv[i] , "rb")
                name = sys.argv[i]

                q = raw_input("dDo you want to kee the name:'%s'?[YES/no]"%(sys.argv[i]))
                if q == "no" or q == "No" or q == "n":
                        name = raw_input("Enter a name for %s\n--->"%sys.argv[i])
                file_data = pb.upload_file(f , name)


                phone.push_file(**file_data)

if __name__ == "__main__":
        if len(sys.argv) < 2:
                Usage()
        run()
