"""
This module provides an API for accessing the PostalMethods web service.
"""

# Import our generated service stub classes.
import os

from PostalWSSimple_services import *
from mailarep_site.postalmethods.examples.postalmethods.util import deprecated


SUCCESS = -3000

class PmClient:
    """
    This class provides access to the full Postal Methods SOAP API.  Each API
    method is exposed as a method on this class.
    """

    def __init__(self,username,password,workMode="Default"):
        """
        Arguments:
        username - Your PostalMethods username.
        password - Your PostalMethods password.
        workMode - 'Production' indicates the letter should actually 
                   be processed (and not simulated). 'Development' forces 
                   simulated processing. 'Default' inherits the PostalMethods 
                   User's default Work Mode setting (set in the Control Panel)
        """
        
        if username is None:
            raise ValueError("Invalid username")
        self._username = username

        if password is None:
            raise ValueError("Invalid password")
        self._password = password

        workModes = ['Production','Development','Default']
        if workMode not in workModes:
            raise ValueError("Invalid workMode, must be one of %s" % workModes.join())
        self.workMode = workMode

        # Build a proxy to the PostalMethods SOAP service.
        self._proxy = PostalWSSimpleLocator().getPostalWSSimpleSoap()


    def sendLetterV2(self,filename,description):
        """
        Makes a call to the PostalMethods SendLetter API method.
        see http://www.postalmethods.com/method/sendletter

        Arguments:
           filename - The name of the file to send (string).
                      see list of supported file types: 
                      http://www.postalmethods.com/supported
        description - Up to 100 characters. Free text. User may add any 
                      text to help identify the request (UTF8)

        Returns: int
            In case of successful submission, a positive number is 
            returned indicating the letter's unique identifier on 
            the system.
            In case of failure, a negative number is returned 
            indicating the failure reason.
            See the list of Web Service Result Codes:
            http://www.postalmethods.com/statuscodes#webservice
        """
        if not os.path.isfile(filename):
            raise ValueError("Invalid file: " + filename)
        ext = self._getExtension(filename)

        fileBytes = file(filename).read()
        encodedBytes = fileBytes

        # create a request
        req = SendLetterV2SoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MyDescription = description
        req._FileExtension = ext
        req._FileBinaryData = encodedBytes
        req._WorkMode = self.workMode # configured at client creation time
        result = self._proxy.SendLetterV2(req)._SendLetterV2Result
        return result


    def sendLetterAndAddressV2(self,filename,description,
                               attentionLine1,attentionLine2,
                               company,address1,address2,
                               city,state,postalCode,country):
        """
        Makes a call to the PostalMethods SendLetterAndAddress API method.
        see http://www.postalmethods.com/method/sendletterandaddress

        Arguments:
              filename - The name of the file to send (string).
                         see list of supported file types: 
                         http://www.postalmethods.com/supported
           description - Up to 100 characters. Free text. User 
                         may add any text to help identify the request (UTF8)
        attentionLine1 - Non-address data, such as company, name, position, 
                         department, etc. Line will not be printed when 
                         empty. At least one of the attention or company 
                         lines must contain data.
        attentionLine2 - Non-address data, such as name, position, 
                         department, etc.  Line will not be printed when 
                         empty.
               company - Company / Firm name.  At least one of the attention 
                         or company lines must contain data.
              address1 - Up to 45 characters.Main delivery address 
                         (e.g., 123 Main St.) or PO Box.  This line must contain 
                         data.
              address2 - Secondary address unit (i.e., Additional address 
                         elements such as Apartment, Suite, Building, 
                         Room, etc.)
                  city - Up to 30 characters. Use 'FPO' or 'APO' when sending to 
                         U.S. Military destinations.  This line must contain data.
                 state - Up to 30 characters. State or Region. Use 'AE', 'AP' 
                         or 'AA' when sending to U.S. Military destinations
            postalCode - Provide postal code in a format used in the destination 
                         country. When destination country is the USA, use a ZIP+4 
                         code. If ZIP+4 is not provided we will try to add it
               country - Value is required only when destination country is 
                         different than the user's country.
        Returns: int
            In case of successful submission, a positive number is 
            returned indicating the letter's unique identifier on 
            the system.
            In case of failure, a negative number is returned 
            indicating the failure reason.
            See the list of Web Service Result Codes:
            http://www.postalmethods.com/statuscodes#webservice
        """
        if not os.path.isfile(filename):
            raise ValueError("Invalid file: " + filename)
        ext = self._getExtension(filename)

        fileBytes = file(filename).read()
        encodedBytes = fileBytes

        # create a request
        req = SendLetterAndAddressV2SoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MyDescription = description
        req._FileExtension = ext
        req._FileBinaryData = encodedBytes
        req._WorkMode = self.workMode # configured at client creation time
        req._AttentionLine1 = attentionLine1
        req._AttentionLine2 = attentionLine2
        req._Company = company
        req._Address1 = address1
        req._Address2 = address2
        req._City = city
        req._State = state
        req._PostalCode = postalCode
        req._Country = country

        result = self._proxy.SendLetterAndAddressV2(req)._SendLetterAndAddressV2Result
        return result        


    def getLetterStatusV2(self,id):
        """
        Makes a call to the PostalMethods GetLetterStatus API method.
        see http://www.postalmethods.com/method/getletterstatus

        Arguments:
        id - Matches the letter ID provided as the response for the original Web 
             Service request.

        Returns: a tuple of (result code, letter status, description, last update)

        result code - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        description - The text description for the status code of the letter:
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter                      
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        # create a request
        req = GetLetterStatusV2SoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.GetLetterStatusV2(req)._GetLetterStatusV2Result
        return (result._ResultCode,result._Status,result._Description,result._LastUpdateTime)


    def getLetterStatusV2Multiple(self,ids):
        """
        Makes a call to the PostalMethods GetLetterStatus_Multiple API method.
        see http://www.postalmethods.com/method/getletterstatus_multiple

        Arguments:
        ids - Matches the letter IDs provided as the response to the 
              original Web Service requests.
              Number of IDs is limited to 1000 items per query. Additional items 
              will be ignored.
              IDs appearing in the list which are not assigned to the account or 
              to which the user has no permissions to access will be returned in 
              the response with a status code which describes the error and 
              zeroed time stamp

        Returns: a tuple of (result code, [] of status tuples )
                 Each status tuple is of the form (id,status,last update)

        result code - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
                 id - Corresponds to one of the IDs sent in the request
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        description - The text description for the status code of the letter:
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        req = GetLetterStatusV2_MultipleSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = ",".join(str(i) for i in ids)

        result = self._proxy.GetLetterStatusV2_Multiple(req)._GetLetterStatusV2_MultipleResult

        returnVals = []
        if result._LetterStatuses:
            for currRecord in result._LetterStatuses._LetterStatusAndDesc:
                returnVals.append( (currRecord._ID,currRecord._Status,currRecord._Description,currRecord._LastUpdateTime) )

        return (result._ResultCode,returnVals)


    def getLetterStatusRangeV2(self,minId,maxId):
        """
        Makes a call to the PostalMethods GetLetterStatus_Range API method.
        see http://www.postalmethods.com/method/getletterstatus_range

        Arguments:
        minId - Defines the beginning of the range of letter ids to request
                status on.
        maxId - Defines the end of the range of letter ids to request status 
                on.

                Response will provide status of up to 1000 letters per query. 
                Additional items will be ignored. Letters which are not assigned 
                to the account or which the user has no permission to access 
                will not be returned. 

        Returns: a tuple of (result code, [] of status tuples )
                 Each status tuple is of the form (id,status,last update)

         resultCode - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
                 id - Corresponds to one of the IDs sent in the request
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        description - The text description for the status code of the letter:
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        req = GetLetterStatusV2_RangeSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MinID = minId
        req._MaxID = maxId

        result = self._proxy.GetLetterStatusV2_Range(req)._GetLetterStatusV2_RangeResult

        returnVals = []
        if result._LetterStatuses:
            for currRecord in result._LetterStatuses._LetterStatusAndDesc:
                returnVals.append( (currRecord._ID,currRecord._Status,currRecord._Description,currRecord._LastUpdateTime) )

        return (result._ResultCode,returnVals)


    def getLetterDetailsV2(self,id):
        """
        Makes a call to the PostalMethods GetLetterDetails API method.
        see http://www.postalmethods.com/method/getletterdetailsV2

        Arguments:
        id - Matches the ID provided as the response to the original 
             Web Service request.

        Returns: a tuple of (resultCode,id,price,numOfSheets,submitTime,
                             completionTime,orientation,envelope,paper,
                             printColor,printSides,nationalMailing,
                             internationalMailing,workMode)

                          id - Matches the ID requested in this Web 
                               Service request.
                       price - Total price, in US Dollars, of the letter.
                 numOfSheets - Number of sheets of paper inserted to the 
                               envelope.
                  submitTime - Date and time when the letter was submitted 
                               to the PostalMethods service.
              completionTime - Approximate date and time when the letter was 
                               delivered to the postal service.
                 orientation - Portrait or landscape. Orientation used to print 
                               the user's document.
                    envelope - Envelope used for this letter.
                       paper - Paper used for this letter.
                  printColor - Full color or black. Color used for printing this 
                               letter.
                  printSides - Simplex or duplex. Printing method used for this 
                               letter.
             nationalMailing - Mailing priority when sending within the account 
                               country.
        internationalMailing - Mailing priority when sending outside the account 
                               country.
                    workMode - Indicates whether the letter was processed completely 
                               ('Production') or only simulated as a test 
                               ('Development'). In case the letter is in Development 
                               Work Mode, it was not charged and the Price value 
                               only indicates the estimated price for such a letter
        """

        # create a request
        req = GetLetterDetailsV2SoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.GetLetterDetailsV2(req)._GetLetterDetailsV2Result

        return (result._ResultCode,
                result._ID,
                result._Price,
                result._NumOfSheets,
                result._SubmitTime,
                result._CompletionTime,
                result._Orientation,
                result._Envelope,
                result._Paper,
                result._PrintColor,
                result._PrintSides,
                result._NationalMailing,
                result._InternationalMailing,
                result._WorkMode)


    def getPDF(self,id,outfilename):
        """
        Makes a call to the PostalMethods GetPDF API method.
        see http://www.postalmethods.com/method/getpdf

        Arguments:
                 id - Matches the ID provided as the response to the original 
                      Web Service request.
        outfilename - The desired filename for the resulting PDF file.

        Returns: int
         resultCode - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
        """

        # create a request
        req = GetPDFSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.GetPDF(req)._GetPDFResult

        # Only write the file if the call succeeded.
        if result._ResultCode == SUCCESS:
            outfile = open(outfilename,"wb")
            outfile.write(result._FileData)
            outfile.close()

        return result._ResultCode


    def cancelDelivery(self,id):
        """
        Makes a call to the PostalMethods CancelDelivery API method.
        see http://www.postalmethods.com/method/canceldelivery

        Arguments:
        id - Matches the ID provided as the response to the original 
             Web Service request.

        Returns: int
         resultCode - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
        """

        req = CancelDeliverySoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.CancelDelivery(req)._CancelDeliveryResult
        return result


    ####
    # Deprecated methods

    @deprecated
    def sendLetter(self,filename,description):
        """
        Makes a call to the PostalMethods SendLetter API method.
        see http://www.postalmethods.com/method/sendletter

        Arguments:
           filename - The name of the file to send (string).
                      see list of supported file types: 
                      http://www.postalmethods.com/supported
        description - Up to 100 characters. Free text. User may add any 
                      text to help identify the request (UTF8)

        Returns: int
            In case of successful submission, a positive number is 
            returned indicating the letter's unique identifier on 
            the system.
            In case of failure, a negative number is returned 
            indicating the failure reason.
            See the list of Web Service Result Codes:
            http://www.postalmethods.com/statuscodes#webservice
        """
        if not os.path.isfile(filename):
            raise ValueError("Invalid file: " + filename)
        ext = self._getExtension(filename)

        fileBytes = file(filename).read()
        encodedBytes = fileBytes

        # create a request
        req = SendLetterSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MyDescription = description
        req._FileExtension = ext
        req._FileBinaryData = encodedBytes
        result = self._proxy.SendLetter(req)._SendLetterResult
        return result


    @deprecated
    def sendLetterAndAddress(self,filename,description,
                             attentionLine1,attentionLine2,
                             company,address1,address2,
                             city,state,postalCode,country):
        """
        Makes a call to the PostalMethods SendLetterAndAddress API method.
        see http://www.postalmethods.com/method/sendletterandaddress

        Arguments:
              filename - The name of the file to send (string).
                         see list of supported file types: 
                         http://www.postalmethods.com/supported
           description - Up to 100 characters. Free text. User 
                         may add any text to help identify the request (UTF8)
        attentionLine1 - Non-address data, such as company, name, position, 
                         department, etc. Line will not be printed when 
                         empty. At least one of the attention or company 
                         lines must contain data.
        attentionLine2 - Non-address data, such as name, position, 
                         department, etc.  Line will not be printed when 
                         empty.
               company - Company / Firm name.  At least one of the attention 
                         or company lines must contain data.
              address1 - Up to 45 characters.Main delivery address 
                         (e.g., 123 Main St.) or PO Box.  This line must contain 
                         data.
              address2 - Secondary address unit (i.e., Additional address 
                         elements such as Apartment, Suite, Building, 
                         Room, etc.)
                  city - Up to 30 characters. Use 'FPO' or 'APO' when sending to 
                         U.S. Military destinations.  This line must contain data.
                 state - Up to 30 characters. State or Region. Use 'AE', 'AP' 
                         or 'AA' when sending to U.S. Military destinations
            postalCode - Provide postal code in a format used in the destination 
                         country. When destination country is the USA, use a ZIP+4 
                         code. If ZIP+4 is not provided we will try to add it
               country - Value is required only when destination country is 
                         different than the user's country.
        Returns: int
            In case of successful submission, a positive number is 
            returned indicating the letter's unique identifier on 
            the system.
            In case of failure, a negative number is returned 
            indicating the failure reason.
            See the list of Web Service Result Codes:
            http://www.postalmethods.com/statuscodes#webservice
        """
        if not os.path.isfile(filename):
            raise ValueError("Invalid file: " + filename)
        ext = self._getExtension(filename)

        fileBytes = file(filename).read()
        encodedBytes = fileBytes

        # create a request
        req = SendLetterAndAddressSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MyDescription = description
        req._FileExtension = ext
        req._FileBinaryData = encodedBytes
        req._AttentionLine1 = attentionLine1
        req._AttentionLine2 = attentionLine2
        req._Company = company
        req._Address1 = address1
        req._Address2 = address2
        req._City = city
        req._State = state
        req._PostalCode = postalCode
        req._Country = country

        result = self._proxy.SendLetterAndAddress(req)._SendLetterAndAddressResult
        return result        


    @deprecated
    def getLetterStatus(self,id):
        """
        Makes a call to the PostalMethods GetLetterStatus API method.
        see http://www.postalmethods.com/method/getletterstatus

        Arguments:
        id - Matches the letter ID provided as the response for the original Web 
             Service request.

        Returns: a tuple of (result code, letter status, last update)

        result code - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        # create a request
        req = GetLetterStatusSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.GetLetterStatus(req)._GetLetterStatusResult
        return (result._ResultCode,result._Status,result._LastUpdateTime)


    @deprecated
    def getLetterStatusMultiple(self,ids):
        """
        Makes a call to the PostalMethods GetLetterStatus_Multiple API method.
        see http://www.postalmethods.com/method/getletterstatus_multiple

        Arguments:
        ids - Matches the letter IDs provided as the response to the 
              original Web Service requests.
              Number of IDs is limited to 1000 items per query. Additional items 
              will be ignored.
              IDs appearing in the list which are not assigned to the account or 
              to which the user has no permissions to access will be returned in 
              the response with a status code which describes the error and 
              zeroed time stamp

        Returns: a tuple of (result code, [] of status tuples )
                 Each status tuple is of the form (id,status,last update)

        result code - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
                 id - Corresponds to one of the IDs sent in the request
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        req = GetLetterStatus_MultipleSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = ",".join(str(i) for i in ids)

        result = self._proxy.GetLetterStatus_Multiple(req)._GetLetterStatus_MultipleResult

        returnVals = []
        if result._LetterStatuses:
            for currRecord in result._LetterStatuses._LetterStatus:
                returnVals.append( (currRecord._ID,currRecord._Status,currRecord._LastUpdateTime) )

        return (result._ResultCode,returnVals)


    @deprecated
    def getLetterStatusRange(self,minId,maxId):
        """
        Makes a call to the PostalMethods GetLetterStatus_Range API method.
        see http://www.postalmethods.com/method/getletterstatus_range

        Arguments:
        minId - Defines the beginning of the range of letter ids to request
                status on.
        maxId - Defines the end of the range of letter ids to request status 
                on.

                Response will provide status of up to 1000 letters per query. 
                Additional items will be ignored. Letters which are not assigned 
                to the account or which the user has no permission to access 
                will not be returned. 

        Returns: a tuple of (result code, [] of status tuples )
                 Each status tuple is of the form (id,status,last update)

         resultCode - Result code for this Web Service request.
                      See the list of Web Service Result Codes:
                      http://www.postalmethods.com/statuscodes#webservice
                 id - Corresponds to one of the IDs sent in the request
             status - The current status code of the letter.
                      See the list of valid Letter Sending Status Codes:
                      http://www.postalmethods.com/statuscodes#letter
        last update - The time stamp of the last update made to the letter's 
                      status.
        """
        req = GetLetterStatus_RangeSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._MinID = minId
        req._MaxID = maxId

        result = self._proxy.GetLetterStatus_Range(req)._GetLetterStatus_RangeResult

        returnVals = []
        if result._LetterStatuses:
            for currRecord in result._LetterStatuses._LetterStatus:
                returnVals.append( (currRecord._ID,currRecord._Status,currRecord._LastUpdateTime) )

        return (result._ResultCode,returnVals)


    @deprecated
    def getLetterDetails(self,id):
        """
        Makes a call to the PostalMethods GetLetterDetails API method.
        see http://www.postalmethods.com/method/getletterdetails

        Arguments:
        id - Matches the ID provided as the response to the original 
             Web Service request.

        Returns: a tuple of (resultCode,id,price,numOfSheets,submitTime,
                             completionTime,orientation,envelope,paper,
                             printColor,printSides,nationalMailing,
                             internationalMailing)

                          id - Matches the ID requested in this Web 
                               Service request.
                       price - Total price, in US Dollars, of the letter.
                 numOfSheets - Number of sheets of paper inserted to the 
                               envelope.
                  submitTime - Date and time when the letter was submitted 
                               to the PostalMethods service.
              completionTime - Approximate date and time when the letter was 
                               delivered to the postal service.
                 orientation - Portrait or landscape. Orientation used to print 
                               the user's document.
                    envelope - Envelope used for this letter.
                       paper - Paper used for this letter.
                  printColor - Full color or black. Color used for printing this 
                               letter.
                  printSides - Simplex or duplex. Printing method used for this 
                               letter.
             nationalMailing - Mailing priority when sending within the account 
                               country.
        internationalMailing - Mailing priority when sending outside the account 
                               country.
        """

        # create a request
        req = GetLetterDetailsSoapIn()
        req._Password = self._password
        req._Username = self._username
        req._ID = id

        result = self._proxy.GetLetterDetails(req)._GetLetterDetailsResult

        return (result._ResultCode,
                result._ID,
                result._Price,
                result._NumOfSheets,
                result._SubmitTime,
                result._CompletionTime,
                result._Orientation,
                result._Envelope,
                result._Paper,
                result._PrintColor,
                result._PrintSides,
                result._NationalMailing,
                result._InternationalMailing)
    ####

    def _getExtension(self,filename):
        if not filename:
            raise ValueError('invalid filename')
        basename = os.path.basename(filename)
        ext = os.path.splitext(basename)[1]
        if not ext:
            raise ValueError("File has no extension: " + filename)
        ext = ext.strip('.').upper()
        return ext
