
# get the python-firebase module NB NOT firebase 
from firebase import firebase
# get a reference for the database
fb=firebase.FirebaseApplication('https://dummyprojliam.firebaseio.com/',None)

# create the data which is a dictionary - a single key:value pair
dummyData={"dummyField1":"dummyValue1"}
# post the data to the dummyData folder as a key value pair
result = fb.post('dummyDataFolder',dummyData)
# the dummyData post automatically gets a key value and the data (dictionary) is the corresponding value ie. key=hash,value=data
print(result)
# the get() method gives back a dictionary of key:value pairs of {key1:data1},{key2:data2}
resultBack= fb.get('dummyDataFolder',None)
print(resultBack)

# list the data (converting dict to str)  by iterating over the keys for each datapoint
for key in list(resultBack.keys()):
    print(str((resultBack[key]))+"\n")
# updating the last data point
print("last key",key)
fb.patch('dummyDataFolder/'+key,
    {"dummyField1":"newData2"})

# updating using put
# put takes three arguments : first is url or path, second is the key name or the snapshot name and third is the data(json)
fb.put('dummyDataFolder/',key,{"dummyField1":"newData3"})

# listing the values of a particular field eg. dummyField1
newRB=resultBack= fb.get('dummyDataFolder',None)
for key in list(newRB.keys()):
    print((newRB[key].get('dummyField1'))+"\n")
    
# deleting a partiuclar datapoint

fb.delete('dummyDataFolder/'+key, None)
print("datapoint " + key +" deleted")
    


