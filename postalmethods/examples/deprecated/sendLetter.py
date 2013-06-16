"""
A simple script to send a sample letter using the PostalMethods 
SendLetter SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""
from postalmethods import client

print 'Testing SendLetter...'
c = client.PmClient('USERNAME','PASSWORD')
result = c.sendLetter('SampleLetter.pdf','My first letter')
print '   Letter was sent with result code: %d' % result

"""
A positive value means the message was successfully queued for processing.
The PostalMethods Letter ID is returned.
 
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
