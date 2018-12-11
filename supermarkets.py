import sys
import math
import matplotlib.pyplot as plt
try:
    supermarket_file = open ("england_supermarket_filtered.csv", "r")
except Exception as e:
      print("Error:  " + str(e))
      sys.exit()
supermarkets = []
for supermarket in supermarket_file:
     supermarket = supermarket.rstrip('\n')
     supermarket_parts = supermarket.split(",")
     supermarket_id = supermarket_parts[0]
     retailer = supermarket_parts[1]
     easting = supermarket_parts[8]
     northing = supermarket_parts[9]
     supermarket = (supermarket_id,retailer,easting,northing)
     supermarkets.append(supermarket)
supermarket_file.close()
#calculate the mean center of all stores for each supermarket

del supermarkets[0] #tp get rid of the first line of the csv file

stores=set([i[1] for i in supermarkets]) #create a unique list of stores

final_list=[]
x_list=[]
y_list=[]
name_list=[]
for i in stores:
	easting=0
	northing=0
	n=0 # counter
	for j in supermarkets:
		if i==j[1] and (len(j[2]) or len(j[3]))>0: #a check not to include the lines with empty easting and northing
			easting =easting + float(j[2])
			northing= northing + float(j[3])
			n+=1
	x=easting/n
	y=northing/n
	final_list.append([i,x,y]) #list with market names and coordinates
	name_list.append(i) #supermarket names
	x_list.append(x) #x coord's
	y_list.append(y) #y coord's
print(final_list) 

fig, ax = plt.subplots(figsize=(10,10))
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
ax.scatter(x_list, y_list)

for i, txt in enumerate(name_list):
    ax.annotate(txt, (x_list[i], y_list[i]))
