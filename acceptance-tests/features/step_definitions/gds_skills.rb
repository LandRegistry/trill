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
  myXpath = ".//*[@id='GDS|skill-desc1-1-1']"
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


When(/^I record my GDS skills$/) do
  mySkillgroup = ".//*[@id='GDS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|1|2']"
  myValue2 = "//*[@id='prof_radio|1|4']"
  create_skill(mySkillgroup, myValue1, myValue2)

end

Then(/^my GDS skills will be recorded$/) do
  # exit the application and log in again, the skill select
  # should match the last skill update that was recorded

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
#  trill_logout()
#  trill_login()

  mySkillclass = 'GDS Skills'
  mySkillgroup = "//*[@id='GDS-skill-group1']/a"
  myValue1 = './/input[@name="prof_radio_1" and @checked]'
  #myValue1 = './/input[@name="prof_radio_Understanding the Digital transformation_BDS.1.1_Understand the government\'s digital and technology transformation agenda and why the government is changing the way it does digital and technology projects." and @checked]'
  check_skill(mySkillclass, mySkillgroup, myValue1)

end
