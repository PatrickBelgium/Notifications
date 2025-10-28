# notifications
generate notifications on your smartphone \

<img width="447" height="164" alt="afbeelding" src="https://github.com/user-attachments/assets/a6ffab2f-4798-49fd-8291-db0a044c7438" />


# Related prerequisites
Python 3.9 version used on a device like Raspberry Pi 2b\
fill in personal data in **'MySecrets.py'** before using the Python code\
Tested on Android devices with third party 'pushsafer' app installed



# Third party needed setup
Create account/register on https://www.pushsafer.com/ \
you receive private key which shall be used in the Python program\
Buy with PayPal min.1000 calls for only 0.99€ (  or even less for more calls ) \
create the Android device ( which have the app intalled ) on your dashboard at pushsafer \
<img width="597" height="178" alt="afbeelding" src="https://github.com/user-attachments/assets/3628d40b-3cf1-4538-8591-51313035b462" />\
Install 'Pushsafer' on your Android device (this will be the 'app' generating the notifications called by your python program to pushsafer provider)\
Finally : test it online before starting with Python coding \
<img width="251" height="261" alt="afbeelding" src="https://github.com/user-attachments/assets/3921006a-7645-4491-ba66-cddb23f9f93a" />

# console results
<img width="678" height="159" alt="afbeelding" src="https://github.com/user-attachments/assets/c1337a0b-dec3-4bca-b4d1-063da162e398" />

# Why third party needed ?
if you dont want to use a third party like 'pushsafer' , you need to do the following setups extra and they are much more work than the price of the notification calls at pushsafer , just to mention....\
> you need to write your own Android app which will handle/create the notifications on your device and also handle communication to a fix IP server or domain name. 
> That server need some code to establish a communication between the request of this python program and your Android application program , and must also be available 24/24

