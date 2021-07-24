#!/usr/bin/python3

import instaloader
import pyfiglet

ascii_banner = pyfiglet.figlet_format("IG-PHOTO")
print(ascii_banner)


ob=instaloader.Instaloader()
user=input("Enter Username ")
ob.download_profile(user, profile_pic_only=True)
