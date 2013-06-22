"""
A simple script to send a sample letter using the 
PostalMethods SendLetterAndAddressV2 SOAP API call.
You must set your SOAP client with a reference to 
the PostalMethods Web Service: 
$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL 
Detailed instructions available in the Python samples zip file
"""
from mailarep_site.postalmethods.examples.postalmethods import client

print 'Testing SendLetterAndAddressV2...'
c = client.PmClient('USERNAME','PASSWORD',workMode="Default")
filename = "SampleLetter.pdf"
result = c.sendLetterAndAddressV2(filename,'SendLetterAndAddress Python Test',
                                'c/o Frank Zappa',  # attionLine1
                                'Accounting Dept.', # attentionLine2,
                                'FZ Music Company', # company
                                '100 Flower Stree', # address1
                                '',                 # address2,
                                'Los Angeles',      # city
                                'CA',               # state
                                '90010',            # postalCode
                                'USA')              # country
print '   Letter was sent with result code: %d' % result

"""
A positive value means the message was successfully queued for processing.
The PostalMethods Letter ID is returned.
 
A negative value means an error occurred.
See the PostalMethods Status Codes: http://www.postalmethods.com/statuscodes#webservice.
"""
