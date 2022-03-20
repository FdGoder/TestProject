from PdfFileHelper import PdfFileHelper


class ReceiptHelper:

    @staticmethod
    def GetPdfReceiptAsDictionary(fileName):
        receiptDictionary = {}

        receiptDataString = PdfFileHelper().GetTextFromPageToString(fileName, 0)
        receiptDataList = receiptDataString.split('\n')

        receiptDictionary["companyName"] = receiptDataList[0]
        receiptDataList.pop(0)

        for line in receiptDataList:
            if not line.strip():
                continue
            key, value = [word.strip() for word in line.split(':')]
            receiptDictionary[key.lower()] = value

        return receiptDictionary
