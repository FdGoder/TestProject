import fitz

from EnvironmentPath import EnvironmentPath


class PdfFileHelper:

    @staticmethod
    def GetTextByFileNameToDictionary(fileName):
        filePath = EnvironmentPath().MyLocalDesktopProjectPath + fileName + '.pdf'
        textByPagesDictionary = {}

        with fitz.open(filePath) as doc:
            for num, page in enumerate(doc.pages()):
                textByPagesDictionary[num] = page.getText()

        return textByPagesDictionary

    def GetTextFromPageToString(self, fileName, pageNumber):
        pdfTextDictionary = self.GetTextByFileNameToDictionary(fileName)
        return pdfTextDictionary[pageNumber]
