import pandas as pd
import logging

class SalesOperation:
    def __init__(self, file, attr, outputFile):
        self.file = file
        self.attr = attr
        self.outputFile = outputFile
        self.salesData = None

    def convertToNumericData(self):
        try:
            self.salesData["price"] = pd.to_numeric(self.salesData["price"], errors='coerce')
        except Exception as e:
            logging.error("Error occured while converting the column values!")

    def readCsvFile(self):
        try:
            self.salesData = pd.read_csv(self.file)
        except Exception as e:
            logging.error("Error occured while reading the input file!")

    def getAveragePrice(self):
        try:
            self.convertToNumericData()
            averagePrice = self.salesData["price"].mean()
            return averagePrice
        except Exception as e:
            logging.error("Error occured while calculating the average price!")

    def filterData(self):
        try:
            averagePrice = self.getAveragePrice()
            self.salesData = self.salesData[self.salesData["price"] < averagePrice]
        except Exception as e:
            logging.error(e)

    def generateOutputFile(self):
        try:
            self.salesData.to_csv(self.outputFile, index=False)
        except Exception as e:
            logging.error("Error occured while generating the output file!")