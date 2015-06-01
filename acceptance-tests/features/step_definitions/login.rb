Given(/^I am logged into Trill$/) do
  visit "#{($TRILL_APPLICATION_URL)}"
  assert page.has_content?("Welcome to Trill")
  first(:xpath, "//*[@id='Login']").click
  trill_login()

end

Given(/^I click on the trill link$/) do
  # no trill link as of yet so will use a visit to the sign in page
  # TRILL_APPLICATION_URL is source from the support/env.rb file
  visit "#{($TRILL_APPLICATION_URL)}"

end


Given(/^I am on the Home Page$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  visit "#{($TRILL_APPLICATION_URL)}"
  assert page.has_content?("Welcome to Trill")

end

Given(/^I select Login$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  first(:xpath, "//*[@id='Login']").click

end

Given(/^I am on my Home Page$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  visit "#{($TRILL_APPLICATION_URL)}"
  assert page.has_content?("Corene")
end





When(/^I login into Trill$/) do
  trill_login()

end

When(/^I am on my Trill homepage$/) do
  # make do visit command - requires an environmental variable (dog )28/4/15
  visit "#{($TRILL_APPLICATION_URL)}"

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

end

When(/^I select to log out record my skills$/) do
  trill_logout()

end

When(/^exit the application$/) do
  trill_logout()

end


When(/^I select Skills$/) do
  #pending # Write code here that turns the phrase above into concrete actions

  first(:xpath, "//*[@id='Skills']").click

end

Then(/^I will go to Skills Page$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  assert page.has_content?("Your GDS skills are")

end


Then(/^I will be on the Login page$/) do
  # check that the page has the text associated with being on the log in page
  assert page.has_content?("Log in to Trill")

end

Then(/^I will see the error message Login incorrect$/) do
  # check that the page has the Username or password is incorrect text associated
  # with an incorrect log in attempt
  assert page.has_content?("Username or password is incorrect")

end

Then(/^I will be returned to the Trill Log In screen$/) do
  # check that the page has the text associated with being on the log in page
  assert page.has_content?("Log in to Trill")

end

Then(/^I will go to my Trill homepage$/) do
  mySignedIn = find(:xpath, ".//*[@id='signed-in-as']").text
  if mySignedIn.include?('Signed in as')
    #puts 'ok'
  else
    puts 'my signed in information =' + mySignedIn
    raise "I am not signed in"
  end

end

Then(/^I can see my first name$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_include function will check then pass or raise
  myXpath = ".//*[@id='name']"
  myValue1 = 'Corene'
  myTestArea = 'First Name'
  check_value_include(myTestArea, myXpath, myValue1)

end

Then(/^I can see my surname$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_include function will check then pass or raise
  myXpath = ".//*[@id='name']"
  myValue1 = 'Eggen'
  myTestArea = 'Surname'
  check_value_include(myTestArea, myXpath, myValue1)

end

Then(/^I can see my role$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_include function will check then pass or raise
  myXpath = "//*[@id='trill-role']"
  myValue1 = 'Service Desk'
  myTestArea = 'GDS Role'
  check_value_include(myTestArea, myXpath, myValue1)

end

Then(/^I will go to the landing page$/) do
  pending # Write code here that turns the phrase above into concrete actions
end
