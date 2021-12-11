#USB History parsing from logs file from OSX

# log file path   /private/var/log/system.log


#file = open("p/private/var/log/system.log", mode="r")

# http://www.linux-usb.org/usb.ids 
import urllib2
#import requests

print "***************************************************************"
print "****************** USB History utiity  ************************"
print "***************************************************************"

def file_apple(file):

    for line in file:

        if 'USBMSC' in line:
        	
        	#print line
    
        	line.split('0x')
        	#print line[2]
        	#print type(line)
        	list  = line.split(' ')
        	#print list
        	#print type(list)
        	#print len(list)
        	print 'UniqueID ===> '+list[9]
        	print '=============================================================='
        	print 'Date and Time ===> 				'+list[0]+' '+list[1]+''+' '+list[2]+' '+list[3]
        	print 'USB device vendor ID (manufacturer) ===> 		'+list[10]
        	print 'product ID (device type) ===> 				'+list[11]
        	print 'device release ( product version) ===> 			'+list[12]
        	print '																		'
        	print '																		'
        	print '																		'


        	
        	#response = requests.get('http://www.linux-usb.org/usb.ids')
        	#print (response.status_code)
        	#print (response.content)

        	#page = response.read()
        	





source = open('/private/var/log/system.log','rb')

apples = file_apple(source)


