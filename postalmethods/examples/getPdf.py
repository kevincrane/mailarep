"""
Simple script to fetch a PDF of a letter using the PostalMethods 
GetPDF SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""

from postalmethods import client

print 'Testing GetPDF...'
c = client.PmClient('USERNAME','PASSWORD')

letterId = 0000000 # Replace with a valid letter ID
result = c.getPDF(letterId, '/tmp/out.pdf')
print str(result)

"""
Result = -3000 means that the data was successfully retrieved.
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
