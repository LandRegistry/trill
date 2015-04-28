require 'capybara'
require 'capybara/dsl'
#require 'rspec'

include Capybara::DSL

Capybara.app_host = 'localhost:4567'
Capybara.default_selector = :css
Capybara.default_driver = :selenium

Capybara.register_driver :selenium do |app|
Capybara::Selenium::Driver.new(app, :browser => :firefox)
end


Given(/^I am a User$/) do
  #pending # Write code here that turns the phrase above into concrete actions
#no step to implement in this sprint (dog 28/4/15)

end

Given(/^I am logged into Trill$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #no step to implement in this sprint (dog 28/4/15)
end


When(/^I login into Trill$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  # login not part of this sprint, this step refelect the required
  # action as a place holder for the actual login story (dog 28/4/15)
  visit "http://localhost:5000/"

end

When(/^I am on my Trill homepage$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  # make do visit command - requires an environmental variable (dog )28/4/15
  visit "http://localhost:5000/"

end

When(/^I click on a collapsed GDS skill group$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  # the default state of the group box is collpased so a single click should
  # ensure the object is in the correct state for the reminder of the test
  click_link("Customer Focus")

end

When(/^I click on an expanded GDS skill group$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  # the default state of the group box is collpased so a double click should
  # ensure the object is in the correct state for the reminder of the test
  click_link("Customer Focus")
  click_link("Customer Focus")

end


Then(/^I will go to my Trill homepage$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  # make do visit command - requires an environmental variable (dog )28/4/15
  visit "http://localhost:5000/"

end

Then(/^I can see my first name$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the first name, put it into a var, check against our known value
  myFirstName = find(:xpath, ".//*[@id='user-name']").text
  if myFirstName != 'Hello ' + "'" +'Maranda Caron'+"'"
    raise "my first name does not match"

end

Then(/^I can see my surname$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the last name, put it into a var, check against our known value
  myLastName = find(:xpath, ".//*[@id='skill-group1']/a").text
  if myLastName != 'Hello ' + "'" +'Maranda Caron'+"'"
    raise "my last name does not match"

end

Then(/^I can see my role$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the user role, put it into a var, check against our known value
  myRole = find(:xpath, "//*[@id='trill-role']").text
  if myRole != 'Your current role is "'"ServiceDesk"'"'
    raise "my role does not match"

end

Then(/^I can see my GDS Skills Title$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the GDS Skills Title, put it into a var, check against our known value
  myGDSskillsTitle = find(:xpath, ".//*[@id='skill-group1']/a").text
  if myGDSskillsTitle != 'Customer Focus'
    raise "my GDS skills title does not match"

end

Then(/^I can see my relevant GDS Skill groups$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the GDS Skills Group, put it into a var, check against our known value
  myGDSskillsGroup = find(:xpath, ".//*[@id='skill-title1-1']").text
  if myGDSskillsGroup != 'Customer is king'
    raise "my GDS skills group does not match"

end

Then(/^the skill group will expand$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the GDS Skills Group expand status value,
  #put it into a var, check against our known value
  myGDSskillsGroup = find(:xpath, ".//*[@id='skill-group1']/a").aria-expanded.text
  if myGDSskillsGroup.upcase != 'TRUE'
    raise "my GDS skills group did not expand"

end

Then(/^I can see the additional skill group information relevant to my role$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the additional GDS Skills Group text,
  #put it into a var, check against our known value
  myAdditionalGDSskillsGroup = find(:xpath, ".//*[@id='skill-group1']/a").text
  if myAdditionalGDSskillsGroup != 'Customer is king'
    raise "my GDS skills group are not visible"

end

Then(/^the skill group will collapse$/) do
  pending # Write code here that turns the phrase above into concrete actions
  myGDSskillsGroup = find(:xpath, ".//*[@id='skill-group1']/a").aria-expanded.text
  if myGDSskillsGroup.upcase != 'FALSE'
    raise "my GDS skills group did not expand"
end

Then(/^I will not see the additional skill group information relevant to my role$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  #get the additional GDS Skills Group text,
  #put it into a var, check against our known value
  myAdditionalGDSskillsGroup = find(:xpath, ".//*[@id='skill-group1']/a").expand.text
  if myAdditionalGDSskillsGroup.upcase != ' '
    raise "my additional GDS skills are visible"

end
