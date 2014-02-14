
class UsersController < ApplicationController
  def webpage
  end

  def add
    if !request.headers["Content-Type"] == "application/json"
      render :json => {}, :status => 500
    end
    my_usr = params[:user]
    my_passwd = params[:password]
    return_code = Users.add(my_usr, my_passwd)
    if return_code < 1
      err_json = {:errCode => return_code}
      render :json => err_json, :status => 200
    else
      return_json = {:errCode => $SUCCESS, :count => return_code}
      render :json => return_json, :status => 200
    end
  end

  def login
    if !request.headers["Content-Type"] == "application/json"
      render :json => {}, :status => 500
    end
    my_usr = params[:user]
    my_passwd = params[:password]
    return_code = Users.login(my_usr, my_passwd)
    if return_code < 1
      err_json = {:errCode => return_code}
      render :json => err_json, :status => 200
    else
      return_json = {:errCode => $SUCCESS, :count => return_code}
      render :json => return_json, :status =>200
    end
  end

  def resetFixture
    
    return_code = Users.TESTAPI_resetFixture
    return_json = {:errCode => return_code}
    render :json =>return_json, :status => 200
  end

  def unitTests
      system("RAILS_ENV=development ruby -Itest test/unit/users_test.rb > test/unit/test_output")
      system("tail -1 test/unit/test_output > test/unit/out")
      output = File.open("test/unit/out")
      output_value = (output.readlines())[0]
      

       # For reference, the last line of the file looks like:
       # "10 tests, 17 assertions, 0 failures, 0 errors, 0 skips"
      failed_tests = Integer(((output_value.split(",")[2]).scan(/\d+/))[0])
      total_tests = Integer(((output_value.split(",")[0]).scan(/\d+/))[0])
      output_json = {:totalTests => total_tests, :nrFailed => failed_tests, :output => (File.open("test/unit/test_output")).read}
      render :json => output_json, :status =>200
  end
end
