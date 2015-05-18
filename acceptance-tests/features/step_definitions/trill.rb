Given(/^I am a User$/) do
  # no step to implement in this sprint (dog 28/4/15)
  # feels very front end driven - log in as 'x' and see 'y'

end

Given(/^I am logged into Trill$/) do
  trill_login()

end


When(/^I login into Trill$/) do
  trill_login()

end

When(/^I am on my Trill homepage$/) do
  # make do visit command - requires an environmental variable (dog )28/4/15
  visit "#{($TRILL_APPLICATION_URL)}/"

end

When(/^I click on a collapsed GDS skill group$/) do
  # the default state of the group box is collpased so a single click should
  # ensure the object is in the correct state for the reminder of the test
  click_link("Basic Digital Skills")
  click_link("Basic Digital Skills")

end

When(/^I click on an expanded GDS skill group$/) do
  # the default state of the group box is collpased so a double click should
  # ensure the object is in the correct state for the reminder of the test
  click_link("Basic Digital Skills")
  click_link("Basic Digital Skills")

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

Then(/^I can see my GDS Skills Title$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_match function will check then pass or raise
  myXpath = ".//*[@id='GDS-skill-group1']/a"
  myValue1 = 'Basic Digital Skills'
  myTestArea = 'GDS Skills Title'
  check_value_match(myTestArea, myXpath, myValue1)

end

Then(/^I can see my relevant GDS Skill groups$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value function will check then pass or raise
  myXpath = ".//*[@id='GDS-skill-group2']/a"
  myValue1 = 'Agile Delivery'
  myTestArea = 'GDS Skills Group'
  check_value_match(myTestArea, myXpath, myValue1)

end

Then(/^the skill group will expand$/) do
  #get the GDS Skills Group expand status value,
  #put it into a var, check against our known value
  myGDSskillsGroup = find(:xpath, ".//*[@id='skill-group1']").attr
  if myGDSskillsGroup != 'TRUE'
    puts myGDSskillsGroup
    raise "my GDS skills group did not expand"
  end
  
end

Then(/^I can see the additional skill group information relevant to my role$/) do
  # pass the xpath, the epected value and the area under test
  # the check_value_include function will check then pass or raise
  myXpath = ".//*[@id='skill-desc1-1-1']"
  myValue1 = 'BDS.1.1 Understand the government'
  myTestArea = 'GDS Additional Skills'
  check_value_include(myTestArea, myXpath, myValue1)

end

Then(/^the skill group will collapse$/) do
  # no easy way to do this, test adds little to nothing to quality assurance

end

Then(/^I will not see the additional skill group information relevant to my role$/) do
  # no easy way to do this, test adds little to nothing to quality assurance

end
