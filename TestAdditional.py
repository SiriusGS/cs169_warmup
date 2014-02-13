import unittest
import os
import testLib

class TestUnit(testLib.RestTestCase):
    """Issue a REST API request to run the unit tests, and analyze the result"""
    def testUnit(self):
        respData = self.makeRequest("/TESTAPI/unitTests", method="POST")
        self.assertTrue('output' in respData)
        print ("Unit tests output:\n"+
               "\n***** ".join(respData['output'].split("\n")))
        self.assertTrue('totalTests' in respData)
        print "***** Reported "+str(respData['totalTests'])+" unit tests. nrFailed="+str(respData['nrFailed'])
        # When we test the actual project, we require at least 10 unit tests
        minimumTests = 10
        if "SAMPLE_APP" in os.environ:
            minimumTests = 4
        self.assertTrue(respData['totalTests'] >= minimumTests,
                        "at least "+str(minimumTests)+" unit tests. Found only "+str(respData['totalTests'])+". use SAMPLE_APP=1 if this is the sample app")
        self.assertEquals(0, respData['nrFailed'])



# Test add users


#
class TestAddSameUser(testLib.RestTestCase):
	def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_USER_EXISTS):
		expected = {'errCode' : errCode}
		if count is not None:
			expected['count'] = count
		self.assertDictEqual(expected, respData)

	def testAdd1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData)

class TestAddNullUsername(testLib.RestTestCase):
	def assertResponse(self, respData, count=None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME):
		expected = {'errCode':errCode}
		if count is not None:
			expected['count']  = count
		self.assertDictEqual(expected, respData)

	def testAdd1(self):
       # self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : "", 'password' : 'password'} )
        self.assertResponse(respData)

class TestLongUsername(testLib.RestTestCase):
	def assertResponse(self, respData, count=None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME):
		expected = {'errCode':errCode}
		if count is not None:
			expected['count']  = count
		self.assertDictEqual(expected, respData)

	def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a' * 129, 'password' : 'password'} )
        self.assertResponse(respData)

class TestBadPassword(testLib.RestTestCase):
	def assertResponse(self, respData, count=None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD):
		expected = {'errCode':errCode}
		if count is not None:
			expected['count']  = count
		self.assertDictEqual(expected, respData)
	def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'a'*129} )
        self.assertResponse(respData)

#Test login
class TestBadCredential(testLib.RestTestCase):
	def assertResponse(self, respData, count= None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS):
		expected = {'errCode':errCode}
		if count is not None:
			expected['count']  = count
		self.assertDictEqual(expected, respData)

	def testLogin1(self):
		respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
		self.assertResponse(respData)


class TestRegisteredLogin(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = 2, errCode = testLib.RestTestCase.SUCCESS):
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData)




















