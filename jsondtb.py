import json
import os.path


basic_jsd = """{ 
"data":[]
}"""

class json_database:
	
	def __init__(self,list_:list,file:str ,id=False):
    		
		# important instances
		self.columns = list_
		self.dbfile = file
        
		#adding the value of id to the list
		list_.append({'id':id})  
		
		#uploading the basic json code to file if file is newly created
		if not os.path.exists(file):
		    basic = json.loads(basic_jsd)
		    with open(file,'w') as f:
			    json.dump(basic,f,indent=2)

		
			
            	
	#methods that lets us view data 	
	def view_data(self):
		with open(self.dbfile,'r') as f:
			db = json.load(f)["data"]
				
		return db

    #methods that lets us view data for class use
	def view_data_class(self):
		with open(self.dbfile,'r') as f:
			db = json.load(f)
		
		return db

	# method that add rows to the database
	def add_row(self,list_:list):
		
		#loading the existing database to work on
		db=self.view_data_class()
        
        # adding the data to the dic
		dic = {}
		for keys,values in zip(self.columns,list_):
			creat = {keys:values}
			dic.update(creat)
        
		try:
		    #if user usses id then add the id
			if self.columns[-1]['id'] == True:
				#get previous id
				db = self.view_data_class()
				old_id = int(db['data'][-1]['id']) #getting old id

				new_id = str(old_id + 1) #setting new id
				dic.update({'id':new_id})

		except:
			dic.update({'id':'1'})

		
		db['data'].append(dic)

		
		
		#saving the aded data back
		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)
	
	#method that delete a dict from the database
	def delete_row(self,column:str,value:str):
		db = self.view_data_class()

		for row in db['data']:
			if row[column] == value:
				db['data'].remove(row)

		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)


	def update_row_element(self,column:str,value_ch:str,
	old_value:str,new_value:str):
		db = self.view_data_class()

		for row in db['data']:
			if row[column] == value_ch:
				row[old_value]=new_value

		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)

		return 'sucess'

	def get_row_elements(self,column:str,value:str):
		db = self.view_data()

		for row in db:
			if row[column] == value:
				return row
		


	
				

	
		

# db2 = json_database(['year','budget'],'summary.json',id=True)

# dbid = json_database(['lalala','latido'],'id.json',id=True)

# dbid.add_row(['205','1600'])
# dbid.update_row_element('lalala','206','lalala','150')
# db2.delete_row('year','2005')





# db= db.view_data()
# print(db)

# for a in dbv:
#     keys = a.keys()
#     values = a.values()

#     for k,v in zip(keys,values):
#     	print(k,' ',v)
    
#     print('_'*13)
