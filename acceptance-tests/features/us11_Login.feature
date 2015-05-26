Feature: Login Trill
# Acceptance Criteria
# - First screen displayed to users will be the Login screen
@US11 @User @Login @Trill
Scenario: Access Trill
Given I click on the trill link
When the Trill application opens
Then I will be on the Login page

#No need to worry about the service being unavailable (Discussed at 3 amigos - 24/4/15).
# - Username and password must be entered to access the system on the Login screen
# - Username = users gsi email address,
#- If default password then request user to supply new password by displaying change of password         # screen
#@US11 @User @Login @Trill
#Scenario: Login First Time
#Given I am a new user
#When I login into Trill
#Then I will be prompted to change my password from the default
#?????What screen will the user after changing their password?????
#?????Will there be any validation?????

# - Password is stored first time and checked subsequently
# - If correct password supplied then access to the Trill system is granted
@US11 @User @Login @Trill
Scenario: Login Second Time
Given I am a User
When I login into Trill
Then I will go to my Trill homepage

# - If username or password is entered then display the error message 'Login incorrect'
@US11 @User @Login @Trill
Scenario: Login Wrong Username
Given I am a User
When I login into Trill with the wrong Username
Then I will see the error message Login incorrect

@US11 @User @Login @Trill
Scenario: Login Wrong Password
Given I am a User
When I login into Trill with the wrong Password
Then I will see the error message Login incorrect
