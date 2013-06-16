Welcome to the Postal Methods Python Toolkit!
-------------------------------------------

This project provides a ready-to-use Python module for accessing the 
PostalMethods web service. For information about the PostalMethods 
web service please see: http://www.postalmethods.com/

You will need a PostalMethods developer account to use this toolkit.
If you don't have an account, please create one here: 
https://cp.postalmethods.com/public/DeveloperRegistration.aspx

You must have Python installed with the Zolera SOAP Infrastructure (ZSI)
module to use this toolkit.

Getting Started.
* The examples directory in this toolkit contains several simple Python
  programs that exercise each of the methods in the PostalMethods SOAP
  service.  To run them, you will have to make sure the postalmethods 
  Python module is on your PYTHONPATH and you will have to edit each 
  program to provide your username and password and possibly other
  information.  These examples are a good place to start.

In a Nutshell.
* The postalmethods Python module needs to be on your PYTHONPATH.
* Usage of the library is simple, just create an instance of PmClient 
  and call its methods which correspond to the web service calls provided by
  the PostalMethods web service.  Here's an example:

from postalmethods import client

print 'Testing SendLetter...'
c = client.PmClient('USERNAME','PASSWORD')
result = c.sendLetter('SampleLetter.pdf','My first letter')
print '   Letter was sent with result code: %d' % result

More Information.
* The PyDoc information for the PmClient class is a good place to 
  look for more details.
* The PostalMethods user support forums are a great place to get more 
  information and help using this toolkit and the PostalMethods web
  service: http://www.postalmethods.com/forums

Build Details.
* SOAP interface classes were generated with the ZSI tool wsdltopy
  invoked as shown below:

$ wsdl2py --url https://api.postalmethods.com/PostalWS.asmx?WSDL
