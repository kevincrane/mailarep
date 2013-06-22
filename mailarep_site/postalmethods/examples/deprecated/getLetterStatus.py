"""
Simple script to get a letter's current status using the PostalMethods 
GetLetterStatus SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""

from mailarep_site.postalmethods.examples.postalmethods import client

print 'Testing GetLetterStatus...'
c = client.PmClient('USERNAME','PASSWORD')

letterId = 0000000 # Replace with a valid letter ID.
print '   Result: ' + str(c.getLetterStatus(letterId))

"""
Result = -3000 means that the data was successfully retrieved.
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
