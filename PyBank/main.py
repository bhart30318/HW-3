#import os and CSV to read file
import os, os.path
import csv

list = os.listdir("./raw_data")
number_files = len(list)

# Grab Budget CSV files
for numbers in range(number_files):
    budgetcsv = os.path.join('raw_data',"budget_data_" + str(numbers+1) + ".csv")
    #Set empty list variables
    date = []
    revenue =[]
    month = []
    year =[]
    revenueChange =[]
    TotalRev =0
    TotalRevChange = 0
    RevBeg=0
    itemCount = 0
    
    # Open raw data file 1
    with open(budgetcsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        #skip headers
        next(csvReader, None)
        
        for row in csvReader:        
            #Append data from the row
            itemCount = itemCount + 1
            date.append(row[0])
            revenue.append(int(row[1]))
            TotalRev = TotalRev + int(row[1])
            RevEnd = int(row[1])
            RevChg = RevEnd - RevBeg
            TotalRevChange = TotalRevChange + RevChg
            revenueChange.append(RevChg)
            splitdate = row[0].split('-')
            month.append(str(splitdate[0]))
            year.append(splitdate[1][-2:])
            RevBeg = RevEnd
    
    AveRevChg = TotalRevChange / itemCount
    GIncrease = max(revenueChange)
    GDecrease = min(revenueChange)
    IncreaseDate = date[revenueChange.index(GIncrease)]
    DecreaseDate = date[revenueChange.index(GDecrease)]
    CountM = len(set(date))
    
    with open('financial_analysis_report_' + str(numbers+1) + '.txt', 'w') as text:
        text.write("Financial Analysis for file 'budget_data_"+ str(numbers+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(CountM) + "\n")
        text.write("    Total Revenue: " + "$" + str(TotalRev) +"\n")
        text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg)) +'\n')
        text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
        text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")