Feature: Edit IS Skills

# US21 - Record IS Skills
# As a user of Trill I want to be able to record my competence against IS Systems
# so that resource management can find me.

# US42 - Viewing my IS skills
# As a Service Desk user
# I want to view my IS skills
# so I can view the IS skills relevant to my role

# Description: The ability to view what I input as my IS Skills
# so that the user can see what they last input
# Title: IS Skills View for Service Desk
# Acceptance Criteria:
# - The screen should display a title for the IS skills section
# - All data/names/skills on the page should come from the database
# - must mirror gds data display wise


@US21 @US42 @User @IS @Trill
Scenario: Record IS Skills
Given I am a User
And I am logged into Trill
And I select Skills
When I record my IS skills
And exit the application
And I log back into Trill
And I select Skills
Then my IS skills will displayed
