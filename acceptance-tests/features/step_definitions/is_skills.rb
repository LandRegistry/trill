Given(/^I select a Skill known to be held as Expert$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio||CSRK.1.1|1']"
  myValue2 = "//*[@id='prof_radio|xxxxxxxxxxxxxxxxxxxxxxxx|CSRK.1.1|4']"
  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select a Skill known to be held as Proficient$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio||CSRK.2.1|1']"
  myValue2 = "//*[@id='prof_radio|fdssfdfdsdfs|CSRK.2.1|3']"

end

Given(/^I select Skill known to be held as None$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio||CSRK.3.1|1']"
  myValue2 = "//*[@id='prof_radio|fgg|CSRK.3.1|2']"

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
