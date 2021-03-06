# log in using known user
def trill_login()
  #visit "#{($TRILL_APPLICATION_URL)}"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'

end


# try to log in using either an incorrct username or password passed in as a var
def trill_bad_login(username, password)
  #visit "#{($TRILL_APPLICATION_URL)}"
  #puts 'on page'
  fill_in('username', :with => username)
  #puts 'on username'
  fill_in('password', :with => password)
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
end


# click the signed in menu object then click log out
def trill_logout()
  # log out
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
end


# create a skill in a skill group
def create_skill(mySkillgroup, myValue1, myValue2)
  # open a list of skills
  first(:xpath, mySkillgroup).click
  # set first skill level
  first(:xpath, myValue1).click
  # set second skill level
  first(:xpath, myValue2).click
  # create a var to hold the selected radio button option to check against the returned result later
  @myRadioButton = find(myValue2).value
  #puts @myRadioButton
end


# check a created a skill in a skill group
def check_skill(mySkillclass, mySkillgroup, myValue1)
  # open the skill group you want to check
  first(:xpath, mySkillgroup).click

  # check whether the last updated skill value has been retained
  # the code below finds the value that matches myValue1 =  a radio button and being checked
  # check that it matches the value set in the create_skill function
  if find(myValue1).value ==  @myRadioButton #'option4'
     #puts "The recorded skill has not been returned:" + mySkillclass
   else
     raise "The recorded skill has not been returned:" + mySkillclass
  end
end


# check that a field value matches the expected value exactly
def check_value_match(myTestArea, myXpath, myValue1)
  myTextToTest = find(:xpath, myXpath).text
  if myTextToTest != myValue1
    puts 'my value = *' + myTextToTest + '* test area = *' + myTestArea
    raise "my test value does not match" + myTestArea
  end
end


# check that a field value includes the expected value
def check_value_include(myTestArea, myXpath, myValue1)
  myTextToTest = find(:xpath, myXpath).text
  if myTextToTest.include?(myValue1)
  #  puts 'passing - my value =' + myTextToTest + ' test area = ' + myTestArea
  else
    puts 'my value = *' + myTextToTest + '* test area = *' + myTestArea
    raise "my test value does not match" + myTestArea
  end
end

def select_skill(myXpath, mySkill)
  #select skill or knowledge from the skill group dropdown
  #sleep(10)
    sleep(1)
    find(:xpath, myXpath).click
    find(:xpath, myXpath).select(mySkill)
    find(:xpath, myXpath).click

end

def select_skill_description(myXpath, myDescription)
  #select skill or knowledge from the skill group dropdown
  #sleep(10)
    sleep(1)
    find(:xpath, myXpath).click
    find(:xpath, myXpath).select(myDescription)
    find(:xpath, myXpath).click

end


def check_report_result(myResultXpath, mySkillValue)
  # find the name associated with the first row on the resource report, check it matches our value
  # check the value held in the first column of the first row of the report matches our expected value
  myReportName = find(:xpath, ".//*[@id='1']").text
  if myReportName == "Corene Eggen"
    #check the value
    mySkillValueToTest = find(:xpath, myResultXpath).text
    if mySkillValueToTest == mySkillValue
      #puts 'found skill'
    else
      # mismatch of proficiency value
      raise "my expected return result should be expert - test value does not match =*" + mySkillValueToTest + "*"
    end
  else
    # mismatch of name
    raise "my reporting test value name does not match Corene Eggen, it is *" + myReportName + "*"
  end

end
