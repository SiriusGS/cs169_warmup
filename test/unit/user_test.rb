require 'test_helper'

$SUCCESS = 1
$ERR_BAD_CREDENTIALS = -1
$ERR_USER_EXISTS = -2
$ERR_BAD_USERNAME = -3
$ERR_BAD_PASSWORD = -4

class UsersTest < ActiveSupport::TestCase

		test "TESTAPI_resetFixture" do
        	Users.TESTAPI_resetFixture
        	result = Users.TESTAPI_resetFixture
        	assert result == $SUCCESS
    	end


	
		test "add legal user" do 
			Users.TESTAPI_resetFixture
			result = Users.add("hello", "world")
			assert result == $SUCCESS, "Adding legal user! Test Failed!"
		end


		test "add blank user" do
			Users.TESTAPI_resetFixture
			result = Users.add("", "test")
			assert result == $ERR_BAD_USERNAME, "Blank user name! Test Failed!"
		end

		test "add long username" do 
			Users.TESTAPI_resetFixture
			result = Users.add("a" * 129, "test")
			assert result = $ERR_BAD_USERNAME, "Long username! Test Failed!"
		end

		test "add long password" do
			Users.TESTAPI_resetFixture
			result = Users.add("s", "a" * 129)
			assert result = $ERR_BAD_PASSWORD, "Long password! Test Failed!"
		end

		test "add duplicate user" do
	 		Users.TESTAPI_resetFixture
	 		result = Users.add("a","test")
	 		assert result == $SUCCESS, "Adding legal user!"
	 		result = Users.add("a","testtty")
	 		assert result == $ERR_USER_EXISTS, "Add duplicate user! Test failed!"
	 	end

	 	test "add different users with same password" do 
	 		Users.TESTAPI_resetFixture
	 		result = Users.add("a", "test")
	 		assert result == $SUCCESS, "Adding legal user! Test failed!"
	 		result = Users.add("s","test")
	 		assert result == $SUCCESS, "Adding legal user! Test failed!"
	 	end

		test "login succeeds" do 
			Users.TESTAPI_resetFixture
			result = Users.add("a","test")
			assert result == $SUCCESS, "Adding legal user! Test failed!"
			result = Users.login("a", "test")
			assert result == 2, "login unexpectedly failed"
		end
	
		test "login fails" do
			Users.TESTAPI_resetFixture
			result = Users.add("a","test")
			assert result == $SUCCESS, "Adding legal user! Test failed"
			result = Users.login("", "")
			assert result == $ERR_BAD_CREDENTIALS, "login doesn't fail as expected"
		end
	
		test "login fails with wrong password" do
			Users.TESTAPI_resetFixture
			result = Users.add("a","test")
			assert result == $SUCCESS, "Adding legal user! Test failed"
			result = Users.login("a", "b" * 129)
			assert result == $ERR_BAD_CREDENTIALS, "login doesn't fail as expected"
		end

    
end
