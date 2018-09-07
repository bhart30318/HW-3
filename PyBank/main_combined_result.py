#import os and CSV to read file

import os
import csv

# Combine file and make the formate consistent
    # Grab Budget CSV files
f1 = 'budget_data_1.csv'
f2 = 'budget_data_2.csv'
budgetCSV1 = os.path.join('raw_data',f1)
budgetCSV2 = os.path.join('raw_data',f2)    
    #Set empty list variables
date1 = []
revenue1 =[]
month1 = []
year1 =[]
newdate1 = []
revenueChange1 =[]
Source1 =[]
date2 = []
revenue2 =[]
month2 = []
year2 =[]
newdate2 = []
revenueChange2 =[]
Source2 =[]
TotalRev1 =0
TotalRev2 = 0
TotalRevChange1 = 0
TotalRevChange2 = 0
RevBeg1=0
RevBeg2=0
itemCount1 = 0
itemCount2 = 0

# Open raw data file 1
with open(budgetCSV1,'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
        #skip headers
    next(csvReader, None)
        
    for row in csvReader:        
            #Append data from the row
        itemCount1 = itemCount1 + 1
        date1.append(row[0])
        revenue1.append(int(row[1]))
        TotalRev1 = TotalRev1 + int(row[1])
        RevEnd1 = int(row[1])
        RevChg1 = RevEnd1 - RevBeg1
        TotalRevChange1 = TotalRevChange1 + RevChg1
        revenueChange1.append(RevChg1)
        Source1.append(f1)
        splitdate1 = row[0].split('-')
        month1.append(str(splitdate1[0]))
        year1.append("20"+splitdate1[1])
        newdate1.append(str(splitdate1[0])+'-'+"20"+splitdate1[1])
        RevBeg1 = RevEnd1
# Open raw data file 2
with open(budgetCSV2,'r') as csvFile:     
    csvReader = csv.reader(csvFile, delimiter=',')
        #skip headers
    next(csvReader, None)
        
    for row in csvReader:                    
            #Append data from the row
        itemCount2 = itemCount2 + 1
        date2.append(row[0])
        revenue2.append(int(row[1]))
        TotalRev2 = TotalRev2 + int(row[1])
        RevEnd2 = int(row[1])
        RevChg2 = RevEnd2 - RevBeg2
        TotalRevChange2 = TotalRevChange2 + RevChg2
        revenueChange2.append(RevChg2)
        Source2.append(f2)
        splitdate2 = row[0].split('-')
        month2.append(str(splitdate2[0]))
        year2.append(str(splitdate2[1]))
        newdate2.append(str(splitdate2[0]+'-'+splitdate2[1]))
        RevBeg2 = RevEnd2

#combining results from two file
Source = Source1 + Source2
Date = date1 + date2
Revenue = revenue1 + revenue2
Month = month1 + month2
Year = year1 + year2
NewDate = newdate1 + newdate2
TotalRev = TotalRev1 + TotalRev2
itemCount = itemCount1 + itemCount2
revenueChange = revenueChange1 + revenueChange2
TotalRevChange = TotalRevChange1 + TotalRevChange2

#Calculate for analysis
AveRevChg1 = TotalRevChange1 / itemCount1
AveRevChg2 = TotalRevChange2 / itemCount2
AveRevChg = TotalRevChange / itemCount
GIncrease1 = max(revenueChange1)
GIncrease2 = max(revenueChange2)
GIncrease = max(revenueChange)
GDecrease1 = min(revenueChange1)
GDecrease2 = min(revenueChange2)
GDecrease = min(revenueChange)
IncreaseDate1 = newdate1[revenueChange1.index(GIncrease1)]
IncreaseDate2 = newdate2[revenueChange2.index(GIncrease2)]
IncreaseDate = NewDate[revenueChange.index(GIncrease)]
DecreaseDate1 = newdate1[revenueChange1.index(GDecrease1)]
DecreaseDate2 = newdate2[revenueChange2.index(GDecrease2)]
DecreaseDate = NewDate[revenueChange.index(GDecrease)]

#Create Combined CSV File
combine = zip(Source,Date, Revenue, Month, Year, NewDate,revenueChange)
CombinebudgetCSV = os.path.join('Combined_budget_data.csv')
with open(CombinebudgetCSV,'w',newline="") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=',')
    csvWriter.writerow(['FileSource','Date','Revenue','Month','Year','NewDate','RevenueChange'])
    csvWriter.writerows(combine)

#Get unique value of Year-Months:
CountM1 = len(set(newdate1))
CountM2 = len(set(newdate2))
CountM = len(set(NewDate))

#Create text file to export results
with open('financial_analysis_report_combined.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(" From file " + f1 +":\n")
    text.write("------------------------------------------\n")
    text.write("    Total Months: " + str(CountM1) + "\n")
    text.write("    Total Revenue: " + "$" + str(TotalRev1) +"\n")
    text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg1)) +'\n')
    text.write("    Greatest Increase in Revenue: " + str(IncreaseDate1) + " ($" + str(GIncrease1) + ")\n")
    text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate1) + " ($" + str(GDecrease1) + ")\n\n")
    text.write(" From file " + f2 +":\n")
    text.write("------------------------------------------\n")
    text.write("    Total Months: " + str(CountM2) + "\n")
    text.write("    Total Revenue: " + "$" + str(TotalRev2) +"\n")
    text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg2)) +'\n')
    text.write("    Greatest Increase in Revenue: " + str(IncreaseDate2) + " ($" + str(GIncrease2) + ")\n")
    text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate2) + " ($" + str(GDecrease2) + ")\n\n")
    text.write(" From both files " +f1 + " and " + f2 + ":\n")
    text.write("------------------------------------------\n")
    text.write("    Total Months: " + str(CountM) + "\n")
    text.write("    Total Revenue: " + "$" + str(TotalRev) +"\n")
    text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg)) +'\n')
    text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
    text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")   

