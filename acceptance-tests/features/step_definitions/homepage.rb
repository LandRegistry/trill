#@US60 @USHome_Page1
#Scenario:  Select Skills on Home Page
#Scenario:  Select Resource on Home Page
#Scenario:  Select Record Skills on Home Page


Given(/^I am not logged in$/) do
  assert page.has_content?("Login")
end

When(/^I am prompted to login$/) do
    assert page.has_content?("Log in to Trill")
end

Then(/^I will go to Skills page$/) do
  myXpath = ".//*[@id='name']"
  myValue1 = 'Eggen'
  myTestArea = 'Surname'
  check_value_include(myTestArea, myXpath, myValue1)
end


Given(/^I select Resource$/) do
  first(:xpath, "//*[@id='Resource']").click
end

Then(/^I will go to Resource page$/) do
  assert page.has_content?("No results to display")
end


Given(/^I select Record Skills$/) do
  first(:xpath, "//*[@id='Record_Skills']").click
end
