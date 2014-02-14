import sys
import unittest
import os
import testLib

# Test 1
class TestFixtureReset(testLib.RestTestCase):
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.makeRequest("/TESTAPI/resetFixture", method="POST")

        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData)

# Test 2

class TestUnregisteredLogin(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData)

# Test 3

class TestDuplicateUserAddition(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_USER_EXISTS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'pass'} )
        self.assertResponse(respData)

# Test 4

class TestBlankUsername(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : "", 'password' : 'password'} )
        self.assertResponse(respData)

# Test 5

class Test129CharUsername(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a' * 129, 'password' : 'password'} )
        self.assertResponse(respData)


# Test 6

class Test129CharPassword(testLib.RestTestCase):
    
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'a'*129} )
        self.assertResponse(respData)

#Test 7

class TestRegisteredLogin(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = 2, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : ''} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : ''} )
        self.assertResponse(respData)

#Test 8

class TestWrongLoginPassword(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'hello'} )
        self.assertResponse(respData)

#Test 9

class TestIntegration(testLib.RestTestCase):
   
    def assertResponse(self, respData, count = 2 , errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData)