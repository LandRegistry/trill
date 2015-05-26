Feature: View Recorded GDS Skills
# Acceptance Criteria
# - Screen should display all previously completed skill abilities

@US20 @User @GDSskills @Trill
Scenario: View Recorded GDS Skills
Given I am a User
And I am logged into Trill
When I record my GDS skills
Then I will see all my recorded GDS skills
