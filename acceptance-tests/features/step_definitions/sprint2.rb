Given(/^I click on the trill link$/) do
  # no trill link as of yet so will use a visit to the sign in page
  visit "http://localhost:5000/signin"
end


When(/^I login into Trill with the wrong Username$/) do
  visit "http://localhost:5000/signin"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Test@landregistry.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
end

When(/^I login into Trill with the wrong Password$/) do
  visit "http://localhost:5000/signin"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Eggen@landregistry.gsi.gov.uk')
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
  pending # Write code here that turns the phrase above into concrete actions
end

When(/^exit the application$/) do
  pending # Write code here that turns the phrase above into concrete actions
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
  pending # Write code here that turns the phrase above into concrete actions
end

Then(/^my GDS skills will displayed$/) do
  pending # Write code here that turns the phrase above into concrete actions
end

Then(/^I will see all my recorded GDS skills$/) do
  pending # Write code here that turns the phrase above into concrete actions
end
