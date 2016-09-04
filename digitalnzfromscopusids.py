#!/usr/bin/python
import requests 
import json 
import re 
import time



scopusAPIkey = 'pop your scopus API key here'
scopusResults = 'file with all your scopus results, including handles'
digNZResults = 'filename with the results from digital nz'

url = 'http://api.digitalnz.org/v3/records.json?api_key='+scopusAPIkey+'&text='

# import our Scopus results

with open(scopusResults, 'r') as f:
	for line in f: #take our results line by line
		time.sleep(.1) #give digital NZ some time so we don't hammer them
		scopusid = line[:23]
		handle = re.search('\d{1,5}\/\d{1,5}', line) # do we have a handle like thing in the line?

		if handle: # if we have found a handle like thing
			with open(digNZResults, 'a') as results: #open our results file
				handlestem = handle.group(0)
				r = requests.get(url+'"handle.net/'+handlestem+'"') # search for the handle in digital NZ
				try:
					recordData=json.loads(r.text) #load the search results into a json object
					try:
						output = recordData['search']['results'][0] #hunt inside the json for our research output
						outputThesislevel = output.get('thesis_level')
						if (outputThesislevel): #is it a thesis with a level (doctoral...)
							thesislevel = outputThesislevel
						else:	
							thesislevel = 'none'
						outputType = output.get('dc_type')
						for string in outputType:
							types = string +":"
						outputDate = output.get('date')	#what date has the output
						if (outputDate):
							date = outputDate[0]
						else:
							date = "none"
						
						outputCreated = output.get('created_at') #when created at digital nz)
						outputString = handlestem+"\t"+types+"\t"+thesislevel+"\t"+date+"\t"+outputCreated+"\t"+scopusid
					except:
						ouptputString = handlestem+"\t"+"no data"+"\t"+scopusid
				except:
					ouptputString = handlestem+"\t"+"no data"+"\t"+scopusid
				print(outputString)
				results.write(outputString+"\n") # write the outputs to our results file
			results.close()
		else:
			print('NO HANDLE*************************************')
f.close()




