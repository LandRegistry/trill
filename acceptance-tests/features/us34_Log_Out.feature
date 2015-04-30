Feature: Trill Log Out
# Acceptance Criteria
# - Logout button which when pressed will log the user out of the system & return them to the Login page
# - Login button must be displayed in the top right hand corner
# - Login button must be displayed in a ribbon along the top of each screen (because other screens will
#   be built into the screen later)

@US34 @User @Logout @Trill @TrillRegress
Scenario: Record GDS Skills
Given I am a User
And I am logged into Trill
When I select to log out record my skills
Then i will be returned to the Trill Log In screen
