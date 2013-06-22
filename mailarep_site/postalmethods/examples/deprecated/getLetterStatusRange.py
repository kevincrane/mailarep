"""
Simple script to fetch the status of multiple letters at once using 
the PostalMethods GetLetterStatus_Range SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""

from mailarep_site.postalmethods.examples.postalmethods import client

print 'Testing GetLetterStatusRange...'
c = client.PmClient('USERNAME','PASSWORD')

minLetterId = 0000000 # Replace with a valid letter ID
maxLetterId = 0000001 # Replace with a valid letter ID

result = c.getLetterStatusRange(minLetterId,maxLetterId)
print str(result)

"""
Result = -3000 means that the data was successfully retrieved.
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
