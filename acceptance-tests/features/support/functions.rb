def trill_login()
  visit "#{($TRILL_APPLICATION_URL)}/signin"
  #puts 'on page'
  fill_in('username', :with => 'Corene.Eggen@land.gsi.gov.uk')
  #puts 'on username'
  fill_in('password', :with => 'Goat')
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'

end



def trill_bad_login(username, password)
  visit "#{($TRILL_APPLICATION_URL)}/signin"
  #puts 'on page'
  fill_in('username', :with => username)
  #puts 'on username'
  fill_in('password', :with => password)
  #puts 'on password'
  first(:xpath, "//*[@id='login-button']").click
  #puts 'clicked button'
end



def trill_logout()
  # log out
  first(:xpath, "//*[@id='signed-in-as']").click
  #puts 'click user in menu bar'
  first(:xpath, "//*[@id='logout-dropdown']").click
  #puts 'logout in the drop down menu'
end
