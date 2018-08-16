from datetime import datetime, timedelta
import csv

file = "../data/rates.txt"

def timeStamper():
    currentTime = datetime.now()

    with open('../data/heart-rate.csv' , 'w') as csvfile:
        fieldNames = ['timestamp' , 'heartrate']
        writer = csv.DictWriter(csvfile , fieldnames=fieldNames)
        writer.writeheader()


        with open(file , "r") as in_file:
            line = in_file.readline().replace("\n","").replace("\n\r","")
            while line:
                currentTime = currentTime + timedelta(minutes = 5)
                myTime = currentTime.strftime("%Y-%m-%d %H:%M:%S.%f")
                taggedLine = myTime + "," + line
		print taggedLine
                writer.writerow({'timestamp': myTime, 'heartrate':line})
                line = in_file.readline().replace("\n","").replace("\n\r","")
print "csv succesfully created"



if __name__ == "__main__":
    timeStamper()
