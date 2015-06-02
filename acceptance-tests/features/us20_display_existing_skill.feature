Feature: View Recorded GDS Skills
# Acceptance Criteria
# - Screen should display all previously completed skill abilities

@US20 @User @GDSskills @Trill
Scenario: View Recorded GDS Skills
Given I am a User
And I am logged into Trill
And I select Skills
When I record my GDS skills
And exit the application
And I log back into Trill
And I select Skills
Then I will see all my recorded GDS skills
