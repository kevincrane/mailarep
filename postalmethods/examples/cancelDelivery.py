"""
Simple script to cancel a letter using the PostalMethods 
CancelDelivery SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""

from postalmethods import client

print 'Testing CancelDelivery...'
c = client.PmClient('USERNAME','PASSWORD')

letterId = 0000000 # Replace with a valid letter ID
result = c.cancelDelivery(letterId)
print '   CancelDelivery returned result code: %d' % result

"""
Result = -3000 means that the data was successfully retrieved.
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
