Feature: Landing Page
# Acceptance Criteria
# - Second screen displayed to users will be the Landing Page screen

@USLanding_Page
Scenario: Access Landing Page
Given I am a User
When I login into Trill
Then I will go to the landing page
