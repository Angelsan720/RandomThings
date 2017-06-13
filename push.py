#! /usr/bin/env python2

from pushbullet import Pushbullet
import sys
import ConfigParser

def Usage():
        print("Usage: %s [file to upload 1] <file to upload 2> <file upload 3...>")
        sys.exit(0)
def run():
        Config = ConfigParser.ConfigParser()
        Config.read("config")
        TOKEN = Config.get("Pushbullet" , "Token")
        pb = Pushbullet(TOKEN)

        print("getting devices:")
        for i in range(0 , len(pb.devices)):
                print(i , pb.devices[i])
        d = input("\nselect a device:")
        phone = pb.devices[d]

        for i in range(1 , len(sys.argv)):
                with open(sys.argv[i] , "rb") as f:
                        file_data = pb.upload_file(f , sys.argv[i])


                phone.push_file(**file_data)

if __name__ == "__main__":
        if len(sys.argv) < 2:
                Usage()
        run()
