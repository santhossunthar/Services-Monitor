from sales_operations import SalesOperation

def run():
    attr = ["street", "city", "zip", "state", "beds", "baths", "sq__ft", "type", "sale_date", "price", "latitude", "longitude"]
    file = open("assignment data.csv", "r")
    outputFile = 'less_than_avg_price.csv'

    salesOperation = SalesOperation(file, attr, outputFile)
    salesOperation.readCsvFile()
    salesOperation.filterData()
    salesOperation.generateOutputFile()

    return True

if __name__ == "__main__":
    run()