import random
import time

def getRandomDate(startDate,endDate):
    print("Printing random number between",startDate,"and",endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))

    randomTime  = startTime + randomGenerator  * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random date =", getRandomDate("1/1/2010","31/12/2024"))