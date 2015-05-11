Given(/^I click on the trill link$/) do
  # no trill link as of yet so will use a visit to the sign in page
  visit "http://localhost:5000/signin"
end


When(/^I login into Trill with the wrong Username$/) do
  visit "http://localhost:5000/signin"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Test@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
end

When(/^I login into Trill with the wrong Password$/) do
  visit "http://localhost:5000/signin"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Banana')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
end

When(/^the Trill application opens$/) do
  myLogIn = find(:xpath, ".//*[@id='login-button']").text
  if myLogIn.include?('Log In')
    #puts 'ok'
  else
    puts 'my signed in information =' + mySignedIn
    raise "This is not the log in screen"
  end
end

When(/^I select to log out record my skills$/) do
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
end

When(/^I record my GDS skills$/) do
  # open the list of skills
  first(:xpath, ".//*[@id='skill-group1']/a").click
  # click on one of the radio buttons to create a start datum
  first(:xpath, "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|2']").click
  # click another one of the radio buttons, this will be the test value
  first(:xpath, "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']").click

  # create a var to hold the selected radio button option to check against the returned result later
@myRadioButton = find("//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']").value
  #puts @myRadioButton

end

When(/^exit the application$/) do
  # log out
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
end


Then(/^I will be on the Login page$/) do
  myLoginPage = find(:xpath, ".//*[@id='password']").text
  if myLoginPage != 'Password'
    #puts 'on login page'
  else
    puts 'my login page text is GDS skills group =' + myLoginPage
    raise "not login page"
  end
  #assert page.has_content?("Username or password is incorrect")
  #//*[@id="password"]
end

Then(/^I will see the error message Login incorrect$/) do
  assert page.has_content?("Username or password is incorrect")

end

Then(/^I will be returned to the Trill Log In screen$/) do
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

  # log out
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
  visit "http://localhost:5000/signin"
  # log in
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
  first(:xpath, "//*[@id='skill-group1']/a").click

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
  # log out
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
  visit "http://localhost:5000/signin"
  # log in
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'

  first(:xpath, "//*[@id='skill-group1']/a").click

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
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
  visit "http://localhost:5000/signin"
  # log in
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
  first(:xpath, "//*[@id='skill-group1']/a").click

  # check whether the last updated skill is the samelick another one of the radio buttons, this will be the test valu
  # the coed below finds the value that matches being a radio button and being checked
  # puts find('.//input[@name="prof_radio_Customer is king_1.0_Description Customer_Focus1.0" and @checked]').value

  if find('.//input[@name="prof_radio_Understanding the Digital transformation_BDS.1.1_Understand the government\'s digital and technology transformation agenda and why the government is changing the way it does digital and technology projects." and @checked]').value ==  @myRadioButton #'option4'
     #puts 'found a checked radio button'
   else
     raise "The recorded skill has not been returned"
   end
end
