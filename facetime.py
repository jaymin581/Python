
print "***************************************************************"
print "****************** Facetime History utiity  *******************"
print "***************************************************************"

def file_apple(file):

    for line in file:
        
        #if ' Sending invitation to:' in line:
        if 'Received invite push from:' in line:
            
            #print line
            list = line.split(' ')
            #print list
            print '**********   Received   ************'
            print 'Call type    ===>        '+list[12]
            print 'Call from      ===>        '+list[8]
            print 'Date         ===>        '+list[0]
            print 'Time         ===>        '+list[1]
            print 'TimeStamp    ===>        '+list[2]
            print '************************************'

def file_apple1(file1):
    for line1 in file1:

        if 'Received accept push from' in line1:
            #print line1
            list1 = line1.split(' ')
            #print list1
            print '**********   Dialed   **************'
            print 'Call type    ===>        '+list1[12]
            print 'Call to    ===>        '+list1[8]
            print 'Date         ===>        '+list1[0]
            print 'Time         ===>        '+list1[1]
            print 'TimeStamp    ===>        '+list1[2]
            print '************************************'



def file_apple2(file2):
    for line2 in file2:
        if 'Reject response: 1' in line2:
                            
            list2 = line2.split(' ')
            print list2
            print '*********** Rejected call from *****'
            print 'Call type    ===>        '+'Undefined'
            print 'Call to      ===>        '+list2[12]
            print 'Date         ===>        '+list2[0]
            print 'Time         ===>        '+list2[1]
            print 'TimeStamp    ===>        '+list2[2]        

    

source = open('/Users/Mac/Library/Logs/FaceTime/FaceTime.log','rb')
source1 = open('/Users/Mac/Library/Logs/FaceTime/FaceTime.log','rb')
source2 = open('/Users/Mac/Library/Logs/FaceTime/FaceTime.log','rb') 

apples = file_apple(source)   
apples1 = file_apple1(source1)
apples2 = file_apple2(source)                   


        	
        	#response = requests.get('http://www.linux-usb.org/usb.ids')
        	#print (response.status_code)
        	#print (response.content)

        	#page = response.read()          +list[0]+' '+list[1]+''+' '+list[2]+' '+list[3]"""
        	








