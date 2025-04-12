import requests 
import csv 
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML" 
page = requests.get(url) 
doc = parseString(page.content) 

# Saving content to XML
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

# print out each train code 
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") 
for objTrainPositionsNode in objTrainPositionsNodes: 
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0) 
    traincode = traincodenode.firstChild.nodeValue.strip() 
    # print(traincode)

# Saving train code to CSV
with open('train_code.csv', mode='w', newline='') as train_file: 
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") 
    for objTrainPositionsNode in objTrainPositionsNodes: 
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0) 
        traincode = traincodenode.firstChild.nodeValue.strip()

# print out latitudes
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") 
for objTrainPositionsNode in objTrainPositionsNodes: 
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0) 
    trainlatitude = traincodenode.firstChild.nodeValue.strip() 
    # print(trainlatitude)



