class UsersController < ApplicationController

	
	SUCCESS = 1
	ERR_BAD_CREDENTIALS = -1
	ERR_USER_EXISTS = -2
	ERR_BAD_USERNAME = -3
	ERR_BAD_PASSWORD = -4
	MAX_USERNAME_LENGTH = 128
	MAX_PASSWORD_LENGTH = 128

	def webpage

	end
	
	def add
		if !request.headers["Content-Type"] == "application/json"
      		render :json => {}, :status => 500
      	end

      	errCode = Users.add(params[:user],params[:password])
      	if errCode < 1 
      		err_json = {:errCode => return_code}
			render :json => err_json, :status => 200
      	else
      		return_json = {:errCode => SUCCESS, :count => errCode}
      		render :json => return_json, :status => 200

      	end
    end

	def login
    	if !request.headers["Content-Type"] == "application/json"
      		render :json => {}, :status => 500
      	end
      	errCode = Users.login(params[:user],params[:password])
      	if errCode < 1
      		err_json = {:errCode => return_code}
      		render :json => err_json, :status => 200
      	else
      		return_json = {:errCode => SUCCESS, :count=> return_code}
      		render :json => return_json, :status => 200
      	end
   
	end


	

	def reset
    	return_code = Users.TESTAPI_resetFixture
    	return_json = {:errCode => return_code}
    	render :json =>return_json, :status => 200
	end

  def unitTest
  	system("RAILS_ENV=development ruby -Itest test/unit/users_test.rb > test/unit/test_output")
    system("tail -1 test/unit/test_output > test/unit/out")
    output = File.open("test/unit/out")
    output_value = (output.readlines())[0]
    failed_tests = Integer(((output_value.split(",")[2]).scan(/\d+/))[0])
    total_tests = Integer(((output_value.split(",")[0]).scan(/\d+/))[0])
    output_json = {:totalTests => total_tests, :nrFailed => Fileailed_tests, :output => (File.open("test/unit/test_output")).read}
    render :json => output_json, :status =>200
  end

end

 
