Given(/^I am a Manager$/) do
  pending # Write code here that turns the phrase above into concrete actions
  # no differemtial between user/manager at this stage of development
end

Given(/^I select the reporting tool$/) do
  pending # Write code here that turns the phrase above into concrete actions
  # click the reports option on the menu bar
  # first(:xpath, "//*[@id='reports????']").click

end

Given(/^I select a Skill known to be held as Expert$/) do
  pending # Write code here that turns the phrase above into concrete actions

  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  #  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  #  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|1']"
  #  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']"
  #  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select a Skill known to be held as Proficient$/) do
  pending # Write code here that turns the phrase above into concrete actions

  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  #  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  #  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|1']"
  #  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|3']"
  #  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select Knowledge known to be held as Basic$/) do
  pending # Write code here that turns the phrase above into concrete actions

  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  #  mySkillgroup = ".//*[@id='IS-knowledge-group1']/a"
  #  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|1']"
  #  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|2']"
  #  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select Skill known to be held as None$/) do
  pending # Write code here that turns the phrase above into concrete actions

  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  #  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  #  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']"
  #  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|1']"
  #  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select Knowledge known to be held as None$/) do
  pending # Write code here that turns the phrase above into concrete actions

  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  #  mySkillgroup = ".//*[@id='IS-knowledge-group1']/a"
  #  myValue1 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|4']"
  #  myValue2 = "//*[@id='prof_radio|Understanding the Digital transformation|BDS.1.1|1']"
  #  create_skill(mySkillgroup, myValue1, myValue2)

end


When(/^I record my IS skills$/) do
  # open a skill set via the xpath
  # select radio button 1 then select radio button 2
  # this should ensure that an action is recorded
  # call the create skill function that will create a var for value of the
  # skill radio button that was selected
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio||CSRK.1.1|1']"
  myValue2 = "//*[@id='prof_radio|xxxxxxxxxxxxxxxxxxxxxxxx|CSRK.1.1|4']"
  create_skill(mySkillgroup, myValue1, myValue2)

end

When(/^I record my IS Systems skills$/) do
  pending # Write code here that turns the phrase above into concrete actions
end

When(/^I generate a report$/) do
  pending # Write code here that turns the phrase above into concrete actions
end


Then(/^my IS skills will displayed$/) do
 # log out of the application then log back into the application to refresh everything
  trill_logout()
  trill_login()

  # call the check_skill function that compares currently recorded radio var
  # with the one created in the create_skill function
  # the mySkillclass var is used to provide a helpful error message if things go bang
  # mySkillgroup =  is the same as the skillgroup selected when creating the entry
  # myValue1 find the value of the radio button where the name matches and
  # the radio button is checked
  mySkillclass = 'IS Skills'
  mySkillgroup = "//*[@id='IS-skill-group1']/a"
  myValue1 = './/input[@name="prof_radio_xxxxxxxxxxxxxxxxxxxxxxxx_CSRK.1.1" and @checked]'
  check_skill(mySkillclass, mySkillgroup, myValue1)

end

Then(/^my IS Systems skills will displayed$/) do
  pending # Write code here that turns the phrase above into concrete actions

end

Then(/^I will see a results for the selected Expert Skill$/) do
  pending # Write code here that turns the phrase above into concrete actions

  #trill_logout()
  #trill_login()

  #mySkillclass = 'IS Skills'
  #mySkillgroup = "//*[@id='IS-skill-group1']/a"
  #myValue1 = './/input[@name="myskillname" and @checked]'
  #check_skill(mySkillclass, mySkillgroup, myValue1)

end

Then(/^I will see a results for the selected Proficient Skill$/) do
  pending # Write code here that turns the phrase above into concrete actions

  #trill_logout()
  #trill_login()

  #mySkillclass = 'IS Skills'
  #mySkillgroup = "//*[@id='IS-skill-group1']/a"
  #myValue1 = './/input[@name="myskillname" and @checked]'
  #check_skill(mySkillclass, mySkillgroup, myValue1)

end

Then(/^I will see a results for the selected Basic Knowledge$/) do
  pending # Write code here that turns the phrase above into concrete actions

  #trill_logout()
  #trill_login()

  #mySkillclass = 'IS Skills'
  #mySkillgroup = "//*[@id='IS-skill-group1']/a"
  #myValue1 = './/input[@name="myskillname" and @checked]'
  #check_skill(mySkillclass, mySkillgroup, myValue1)

end

Then(/^I will see a message stating that no results were found for the search$/) do
  pending # Write code here that turns the phrase above into concrete actions

  #assert page.has_content?("No results found for your search")

end
