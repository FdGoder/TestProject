from ReceiptHelper import ReceiptHelper

fileName = "6cbf859a-80e3-4057-8902-4a38ba13886a"
companyName = "ERP.AERO, INC."
errorMessage = "Wrong Company name"

receiptDictionary = ReceiptHelper().GetPdfReceiptAsDictionary(fileName)
assert receiptDictionary["companyName"] == "ERP.AERO, INC.", "Wrong Company name"

print(receiptDictionary)
