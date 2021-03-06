################################################## 
# PostalWSSimple_services.py 
# generated by ZSI.generate.wsdl2python
##################################################


from ZSI import client

from mailarep_site.postalmethods.postalmethods.PostalWSSimple_services_types import *


# Locator
class PostalWSSimpleLocator:
    PostalWSSimpleSoap_address = "https://api.postalmethods.com/PostalWS.asmx"
    def getPostalWSSimpleSoapAddress(self):
        return PostalWSSimpleLocator.PostalWSSimpleSoap_address
    def getPostalWSSimpleSoap(self, url=None, **kw):
        return PostalWSSimpleSoapSOAP(url or PostalWSSimpleLocator.PostalWSSimpleSoap_address, **kw)

# Methods
class PostalWSSimpleSoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: SendLetter
    def SendLetter(self, request):
        if isinstance(request, SendLetterSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/SendLetter", **kw)
        # no output wsaction
        response = self.binding.Receive(SendLetterSoapOut.typecode)
        return response

    # op: SendLetterAndAddress
    def SendLetterAndAddress(self, request):
        if isinstance(request, SendLetterAndAddressSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/SendLetterAndAddress", **kw)
        # no output wsaction
        response = self.binding.Receive(SendLetterAndAddressSoapOut.typecode)
        return response

    # op: GetLetterStatus
    def GetLetterStatus(self, request):
        if isinstance(request, GetLetterStatusSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatus", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatusSoapOut.typecode)
        return response

    # op: GetLetterStatus_Multiple
    def GetLetterStatus_Multiple(self, request):
        if isinstance(request, GetLetterStatus_MultipleSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatus_Multiple", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatus_MultipleSoapOut.typecode)
        return response

    # op: GetLetterStatus_Range
    def GetLetterStatus_Range(self, request):
        if isinstance(request, GetLetterStatus_RangeSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatus_Range", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatus_RangeSoapOut.typecode)
        return response

    # op: GetLetterDetails
    def GetLetterDetails(self, request):
        if isinstance(request, GetLetterDetailsSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterDetails", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterDetailsSoapOut.typecode)
        return response

    # op: GetPDF
    def GetPDF(self, request):
        if isinstance(request, GetPDFSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetPDF", **kw)
        # no output wsaction
        response = self.binding.Receive(GetPDFSoapOut.typecode)
        return response

    # op: CancelDelivery
    def CancelDelivery(self, request):
        if isinstance(request, CancelDeliverySoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/CancelDelivery", **kw)
        # no output wsaction
        response = self.binding.Receive(CancelDeliverySoapOut.typecode)
        return response

    # op: SendLetterV2
    def SendLetterV2(self, request):
        if isinstance(request, SendLetterV2SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/SendLetterV2", **kw)
        # no output wsaction
        response = self.binding.Receive(SendLetterV2SoapOut.typecode)
        return response

    # op: SendLetterAndAddressV2
    def SendLetterAndAddressV2(self, request):
        if isinstance(request, SendLetterAndAddressV2SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/SendLetterAndAddressV2", **kw)
        # no output wsaction
        response = self.binding.Receive(SendLetterAndAddressV2SoapOut.typecode)
        return response

    # op: GetLetterDetailsV2
    def GetLetterDetailsV2(self, request):
        if isinstance(request, GetLetterDetailsV2SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterDetailsV2", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterDetailsV2SoapOut.typecode)
        return response

    # op: GetLetterStatusV2
    def GetLetterStatusV2(self, request):
        if isinstance(request, GetLetterStatusV2SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatusV2", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatusV2SoapOut.typecode)
        return response

    # op: GetLetterStatusV2_Multiple
    def GetLetterStatusV2_Multiple(self, request):
        if isinstance(request, GetLetterStatusV2_MultipleSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatusV2_Multiple", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatusV2_MultipleSoapOut.typecode)
        return response

    # op: GetLetterStatusV2_Range
    def GetLetterStatusV2_Range(self, request):
        if isinstance(request, GetLetterStatusV2_RangeSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="PostalMethods/GetLetterStatusV2_Range", **kw)
        # no output wsaction
        response = self.binding.Receive(GetLetterStatusV2_RangeSoapOut.typecode)
        return response

SendLetterSoapIn = ns0.SendLetter_Dec().pyclass

SendLetterSoapOut = ns0.SendLetterResponse_Dec().pyclass

SendLetterAndAddressSoapIn = ns0.SendLetterAndAddress_Dec().pyclass

SendLetterAndAddressSoapOut = ns0.SendLetterAndAddressResponse_Dec().pyclass

GetLetterStatusSoapIn = ns0.GetLetterStatus_Dec().pyclass

GetLetterStatusSoapOut = ns0.GetLetterStatusResponse_Dec().pyclass

GetLetterStatus_MultipleSoapIn = ns0.GetLetterStatus_Multiple_Dec().pyclass

GetLetterStatus_MultipleSoapOut = ns0.GetLetterStatus_MultipleResponse_Dec().pyclass

GetLetterStatus_RangeSoapIn = ns0.GetLetterStatus_Range_Dec().pyclass

GetLetterStatus_RangeSoapOut = ns0.GetLetterStatus_RangeResponse_Dec().pyclass

GetLetterDetailsSoapIn = ns0.GetLetterDetails_Dec().pyclass

GetLetterDetailsSoapOut = ns0.GetLetterDetailsResponse_Dec().pyclass

GetPDFSoapIn = ns0.GetPDF_Dec().pyclass

GetPDFSoapOut = ns0.GetPDFResponse_Dec().pyclass

CancelDeliverySoapIn = ns0.CancelDelivery_Dec().pyclass

CancelDeliverySoapOut = ns0.CancelDeliveryResponse_Dec().pyclass

SendLetterV2SoapIn = ns0.SendLetterV2_Dec().pyclass

SendLetterV2SoapOut = ns0.SendLetterV2Response_Dec().pyclass

SendLetterAndAddressV2SoapIn = ns0.SendLetterAndAddressV2_Dec().pyclass

SendLetterAndAddressV2SoapOut = ns0.SendLetterAndAddressV2Response_Dec().pyclass

GetLetterDetailsV2SoapIn = ns0.GetLetterDetailsV2_Dec().pyclass

GetLetterDetailsV2SoapOut = ns0.GetLetterDetailsV2Response_Dec().pyclass

GetLetterStatusV2SoapIn = ns0.GetLetterStatusV2_Dec().pyclass

GetLetterStatusV2SoapOut = ns0.GetLetterStatusV2Response_Dec().pyclass

GetLetterStatusV2_MultipleSoapIn = ns0.GetLetterStatusV2_Multiple_Dec().pyclass

GetLetterStatusV2_MultipleSoapOut = ns0.GetLetterStatusV2_MultipleResponse_Dec().pyclass

GetLetterStatusV2_RangeSoapIn = ns0.GetLetterStatusV2_Range_Dec().pyclass

GetLetterStatusV2_RangeSoapOut = ns0.GetLetterStatusV2_RangeResponse_Dec().pyclass
