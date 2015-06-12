Given(/^I select a Skill known to be held as Expert$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|67|1']"
  myValue2 = "//*[@id='prof_radio|67|4']"
  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select a Skill known to be held as Proficient$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|68|1']"
  myValue2 = "//*[@id='prof_radio|68|3']"
  create_skill(mySkillgroup, myValue1, myValue2)
  # uncomment he row below to cause an error which produces an evidence screenshot
  #first(:xpath, "//*[@id='categ111']").click

end

Given(/^I select Skill known to be held as None$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|69|2']"
  myValue2 = "//*[@id='prof_radio|69|1']"
  create_skill(mySkillgroup, myValue1, myValue2)
end


When(/^I record my IS skills$/) do
  # open a skill set via the xpath
  # select radio button 1 then select radio button 2
  # this should ensure that an action is recorded
  # call the create skill function that will create a var for value of the
  # skill radio button that was selected

  mySkillgroup = ".//*[@id='IS-skill-group1']/a"
  myValue1 = "//*[@id='prof_radio|67|1']"
  myValue2 = "//*[@id='prof_radio|67|4']"
  puts ' when i record creating an expert' + 'value 1 =' + myValue1 + 'value 2 ='+myValue2
  create_skill(mySkillgroup, myValue1, myValue2)

end


Then(/^my IS skills will displayed$/) do
  # call the check_skill function that compares currently recorded radio var
  # with the one created in the create_skill function
  # the mySkillclass var is used to provide a helpful error message if things go bang
  # mySkillgroup =  is the same as the skillgroup selected when creating the entry
  # myValue1 find the value of the radio button where the name matches and
  # the radio button is checked
  mySkillclass = 'IS Skills'
  mySkillgroup = "//*[@id='IS-skill-group1']/a"
  myValue1 = './/input[@name="prof_radio_67" and @checked]'
  check_skill(mySkillclass, mySkillgroup, myValue1)

end
