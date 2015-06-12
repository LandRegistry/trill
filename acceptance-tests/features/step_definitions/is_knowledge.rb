Given(/^I select Knowledge known to be held as Basic$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group4']/a"
  myValue1 = "//*[@id='prof_radio|121|1']"
  myValue2 = "//*[@id='prof_radio|121|2']"
  create_skill(mySkillgroup, myValue1, myValue2)

end

Given(/^I select Knowledge known to be held as None$/) do
  # reuse the create_skill(mySkillgroup, myValue1, myValue2)
  mySkillgroup = ".//*[@id='IS-skill-group4']/a"
  myValue1 = "//*[@id='prof_radio|122|4']"
  myValue2 = "//*[@id='prof_radio|122|1']"
  create_skill(mySkillgroup, myValue1, myValue2)

end


When(/^I record my IS Systems skills$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  mySkillgroup = ".//*[@id='IS-skill-group4']/a"
  myValue1 = "//*[@id='prof_radio|121|1']"
  myValue2 = "//*[@id='prof_radio|121|2']" #//*[@id="prof_radio|121|1"]
  create_skill(mySkillgroup, myValue1, myValue2)

end


Then(/^my IS Systems skills will displayed$/) do
  #pending # Write code here that turns the phrase above into concrete actions
  mySkillclass = 'IS Skills'
  mySkillgroup = "//*[@id='IS-skill-group4']/a"
  myValue1 = './/input[@name="prof_radio_121" and @checked]'

  #myValue1 = './/input[@name="prof_radio_9493929190898887dsfgfbvcfghr_TS.1.1" and @checked]'
  check_skill(mySkillclass, mySkillgroup, myValue1)

end
