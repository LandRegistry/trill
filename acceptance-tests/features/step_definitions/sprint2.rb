Given(/^I click on the trill link$/) do
  # no trill link as of yet so will use a visit to the sign in page
  # TRILL_APPLICATION_URL is source from the support/env.rb file
  visit "#{($TRILL_APPLICATION_URL)}/signin"
end


When(/^I login into Trill with the wrong Username$/) do
  username = 'Corene.Test@land.gsi.gov.uk'
  password = 'Goat'
  trill_bad_login(username, password)
end

When(/^I login into Trill with the wrong Password$/) do
  username = 'Corene.Eggen@land.gsi.gov.uk'
  password = 'Banana'
  trill_bad_login(username, password)
end

When(/^the Trill application opens$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_include function will check then pass or raise
  myXpath = ".//*[@id='login-button']"
  myValue1 = 'Log In'
  myTestArea = 'Login open application'
  check_value_include(myTestArea, myXpath, myValue1)

#  myLogIn = find(:xpath, ".//*[@id='login-button']").text
#  if myLogIn.include?('Log In')
    #puts 'ok'
#  else
#    puts 'my signed in information =' + mySignedIn
#    raise "This is not the log in screen"
#  end
end

When(/^I select to log out record my skills$/) do
  trill_logout()
end

When(/^I record my GDS skills$/) do
  mySkillgroup = ".//*[@id='GDS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|2']"
  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']"

  create_skill(mySkillgroup, myValue1, myValue2)

end

When(/^exit the application$/) do
  trill_logout()
end


Then(/^I will be on the Login page$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value function will check then pass or raise
#  myXpath = ".//*[@id='password']"
#  myValue1 = 'Password'
#  myTestArea = 'Login - not login page'
#  check_value_match(myTestArea, myXpath, myValue1)

  myLoginPage = find(:xpath, ".//*[@id='password']").text
  if myLoginPage != 'Password'
    #puts 'on login page'
  else
    puts 'my login page text is GDS skills group =' + myLoginPage
    raise "not login page"
  end
end

Then(/^I will see the error message Login incorrect$/) do
  assert page.has_content?("Username or password is incorrect")

end

Then(/^I will be returned to the Trill Log In screen$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value function will check then pass or raise
#  myXpath = ".//*[@id='password']"
#  myValue1 = 'Password'
#  myTestArea = 'Login - password'
#  check_value_include(myTestArea, myXpath, myValue1)

  myLoginPage = find(:xpath, ".//*[@id='password']").text
  if myLoginPage != 'Password'
    #puts 'on login page'
  else
    puts 'my login page text is GDS skills group =' + myLoginPage
    raise "not login page"
  end
end

Then(/^my GDS skills will be recorded$/) do
  # exit the application and log in again, the skill select
  # should match the last skill update that was recorded
  trill_logout()
  trill_login()

  first(:xpath, "//*[@id='GDS-skill-group1']/a").click

  # check whether the last updated skill is the samelick another one of the radio buttons, this will be the test valu
  # the coed below finds the value that matches being a radio button and being checked
  # puts find('.//input[@name="prof_radio_Customer is king_1.0_Description Customer_Focus1.0" and @checked]').value


 if find('.//input[@name="prof_radio_Understanding the Digital transformation_BDS.1.1_Understand the government\'s digital and technology transformation agenda and why the government is changing the way it does digital and technology projects." and @checked]').value ==  @myRadioButton #'option4'
     #puts 'found a checked radio button'
   else
     raise "The recorded skill has not been returned"
   end

end

Then(/^my GDS skills will displayed$/) do
  trill_logout()
  trill_login()

  first(:xpath, "//*[@id='GDS-skill-group1']/a").click

  # check whether the last updated skill is the samelick another one of the radio buttons, this will be the test valu
  # the coed below finds the value that matches being a radio button and being checked
  # puts find('.//input[@name="prof_radio_Customer is king_1.0_Description Customer_Focus1.0" and @checked]').value

  if find('.//input[@name="prof_radio_Understanding the Digital transformation_BDS.1.1_Understand the government\'s digital and technology transformation agenda and why the government is changing the way it does digital and technology projects." and @checked]').value ==  @myRadioButton #'option4'
     #puts 'found a checked radio button'
   else
     raise "The recorded skill has not been returned"
   end
end

Then(/^I will see all my recorded GDS skills$/) do
  trill_logout()
  trill_login()

  mySkillclass = 'GDS Skills'
  mySkillgroup = "//*[@id='GDS-skill-group1']/a"
  myValue1 = './/input[@name="prof_radio_Understanding the Digital transformation_BDS.1.1_Understand the government\'s digital and technology transformation agenda and why the government is changing the way it does digital and technology projects." and @checked]'
  check_skill(mySkillclass, mySkillgroup, myValue1)

end
