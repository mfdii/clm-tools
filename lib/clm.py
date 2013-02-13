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
		request = {"callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1}
		response, content = http.request(self.endpoint+"/csm/serviceofferinginstance/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
		json_content = loads(content)

		return json_content[0]['results']

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

	def describeTenants(self):
		http=httplib2.Http()
		request =  { "callbackURL":"", "operationParams": [ ], "postCallout":"", "preCallout":"", "timeout":-1  }
		response, content = http.request(self.endpoint+"/csm/Organization/search", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
		json_content = loads(content)
		
		return json_content[0]['results']

	def getTenant(self,tenant):
		http=httplib2.Http()
		response, content = http.request(self.endpoint+"/csm"+tenant, "GET",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken})
		json_content = loads(content)
		return json_content[0]

	def runInstance(self,SOreConID, tenant, quantity=1):

		http=httplib2.Http()
		request =  { "callbackURL":"", "operationParams": [{
				"name" : "serviceOfferingID",
				"value" : {
					"cloudClass" : "com.bmc.cloud.model.beans.ServiceOffering",
  					"reconciliationID" : SOreConID
				},
				"type" : "com.bmc.cloud.model.beans.ServiceOffering",
				"multiplicity" : "1"
				}, {
				"name" : "quantity",
				"value" : quantity,
				"type" : "java.lang.Integer",
				"multiplicity" : "1"
				},{
				"name" : "name",
				"value" : "centos-api",
				"type" : "java.lang.String",
				"multiplicity" : "0..1"
				},{
				"name" : "tenant",
				"value" : tenant,
				"type" : "java.lang.String",
				"multiplicity" : "0..1"
				}
				], "postCallout":"", "preCallout":"", "timeout":-1  }
		response, content = http.request(self.endpoint+"/csm/ServiceOfferingInstance/bulkCreate", "POST",headers={'Accept': 'application/json','User-agent': 'bmc-tools', 'Authentication-Token': self.authToken}, body=dumps(request, indent=2))
		print dumps(request, indent=2)
		print response
		print content
