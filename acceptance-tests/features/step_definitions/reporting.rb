Given(/^I select the reporting tool$/) do
  # click the reports option on the menu bar
  first(:xpath, "//*[@id='Resource']").click

end


When(/^I generate a report expecting results$/) do
  # the report is generated once an entry is slected in the 'skill description'
  # select the skill type - Skill or Knowledge
  # select the skill description

  myXpath = "//*[@id='categ1']"
  mySkill = "Skills"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill1']"
  myDescription = "67 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  myXpath = "//*[@id='categ2']"
  mySkill = "Skills"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill2']"
  myDescription = "68 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  myXpath = "//*[@id='categ3']"
  mySkill = "Knowledge"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill3']"
  myDescription = "121 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  # uncomment he row below to cause an error which produces an evidence screenshot
  # first(:xpath, "//*[@id='categ111']").click

end

When(/^I generate a report expecting no results$/) do
  # the report is generated once an entry is slected in the 'skill description'
  # select the skill type - Skill or Knowledge
  # select the skill description
  
  myXpath = "//*[@id='categ1']"
  mySkill = "Skills"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill1']"
  myDescription = "96 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  myXpath = "//*[@id='categ2']"
  mySkill = "Skills"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill2']"
  myDescription = "102 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  myXpath = "//*[@id='categ3']"
  mySkill = "Knowledge"
  select_skill(myXpath, mySkill)

  myXpath = "//*[@id='skill3']"
  myDescription = "130 - question and answer site for professional and enthusiast programmers. It's 100% free"
  select_skill_description(myXpath, myDescription)

  # uncomment he row below to cause an error which produces an evidence screenshot
  # first(:xpath, "//*[@id='categ111']").click

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
  #pending # Write code here that turns the phrase above into concrete actions
  assert page.has_content?("No results to display")

end
