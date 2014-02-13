'''
$SUCCESS = 1
$ERR_BAD_CREDENTIALS = -1
$ERR_USER_EXISTS = -2
$ERR_BAD_USERNAME = -3
$ERR_BAD_PASSWORD = -4
$MAX_USERNAME_LENGTH = 128
$MAX_PASSWORD_LENGTH = 128

class Users < ActiveRecord::Base
	attr_accessible :username, :password, :count
	def self.login(username, password)
		login = where("username = ? AND password = ?", username, password)
		if login.length > 0
			user = login.first
			user.count = user.count + 1
			user.save
			return user.count
		else 
			return $ERR_BAD_CREDENTIALS 
		end
	end


	def self.add(username, password)
		if Users.exists?(:username => username.to_s)
			return $ERR_USER_EXISTS
		elsif username.nil? or username.to_s == "" or username.length > 128
			return $ERR_BAD_USERNAME
		elsif password.nil? or password.length > 128
			return $ERR_BAD_PASSWORD
		else 
			user = User.new(:username => username, :password=>password, :count => 1)
			user.save
			return user.count
		end
	end

	def self.TESTAPI_resetFixture
		Users.delete_all
		return $SUCCESS
	end
end
'''
class Users < ActiveRecord::Base
	attr_accessible :username, :password, :count

	def self.login(my_usr, my_passwd)
		login_record = where("username = ? AND password = ?", my_usr, my_passwd)
		if login_record.length > 0
			user_record = login_record.first
			user_record.count = user_record.count + 1
			user_record.save
			return user_record.count
		else 
			return $ERR_BAD_CREDENTIALS 
		end
	end


	def self.add(my_usr, my_passwd)
		if Users.exists?(:username => my_usr.to_s)
			return $ERR_USER_EXISTS
		elsif my_usr.nil? or my_usr.to_s == "" or my_usr.length > 128
			return $ERR_BAD_USERNAME
		elsif my_passwd.nil? or my_passwd.length > 128
			return $ERR_BAD_PASSWORD
		else 
			new_user_record = Users.new(:username => my_usr, :password => my_passwd, :count => 1)
			new_user_record.save
			return new_user_record.count
		end
	end

	def self.TESTAPI_resetFixture
		Users.delete_all
		return $SUCCESS
	end
end
'''