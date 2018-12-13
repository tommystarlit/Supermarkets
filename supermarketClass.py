class supermarket (object): # a class for supermarkets
	def __init__(self,supermarket_id,retailer,easting,northing):
		self.supermarket_id = supermarket_id
		self.retailer = retailer
		self.easting = easting
		self.northing = northing
		self.supermarkets=[]
		self.x_list=[]
		self.y_list=[]
		self.final_list=[]
		self.name_list=[]
		self.n=[]
		self.i=[]

	def new_supermarket_list (self):
		for i in range(len(self.final_list)):
			self.easting=0
			self.northing=0
			self.n=0

	def remove_blank (self):
		for j in self.supermarkets:
			if self.i==j[1] and (len(j[2]) or len(j[3]))>0:
				self.easting =self.easting + float(j[2])
				self.northing= self.northing + float(j[3])
				self.n+=1

	def mean_center(self):
		x = self.easting/self.n
		y = self.northing/self.n
		return (x,y)
		self.final_list.append(self.i,self.x,self.y)
		self.name_list.append(self.i)
		return(self.final_list)