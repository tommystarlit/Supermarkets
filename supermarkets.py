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
final_coordinates=[]
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
	final_coordinates.append([x,y]) #list with coordinates only

print(final_list) 
#print(final_coordinates)

#print(*zip(*final_coordinates))
plt.scatter(*zip(*final_coordinates))