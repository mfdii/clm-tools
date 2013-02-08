from json import *
import  httplib2

class CLM:

	authToken = ""
	user=""
	password=""	
	endpoint=""

	def __init__(self,user,password,endpoint):
		self.user=user
		self.password=password
		self.endpoint=endpoint

	def login(self):
		http=httplib2.Http()
		request =  { 'username': self.user, 'password': self.password } 
		response, content = http.request(self.endpoint+"/csm/login", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools'}, body=dumps(request, indent=2))
		self.authToken = response['authentication-token']

	def describeInstances(self):
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/serviceofferinginstance/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
		return content

	def describeImages(self):
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/serviceoffering/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
                json_content = loads(content)
		
		return json_content[0]['results']
	
	
	def describeRegions(self):
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/Location/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
                json_content = loads(content)

		return json_content[0]['results']

	def describeAZs(self):
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/Pod/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
                json_content = loads(content)

		return json_content[0]['results']

	def describeVPCs(self):
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/NetworkContainer/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
                json_content = loads(content)
		
		return json_content[0]['results']

	def runInstance(self,SOguid):

		SOreConID = ""
		http=httplib2.Http()
                request =  { "callbackURL":"", "operationParams": [{ "quantity": 1, "serviceOfferingID": SOreConID }], "postCallout":"", "preCallout":"", "timeout":-1  }
                response, content = http.request(self.endpoint+"/csm/NetworkContainer/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
                json_content = loads(content)
                for serviceOffering in  json_content[0]['results']:
                        print serviceOffering['guid'] + "\t" + serviceOffering['name']
