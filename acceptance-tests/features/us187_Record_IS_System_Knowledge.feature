Feature: Edit IS Systems Skill

# US187 - Record System Knowledge Skills
# US189 - View System Knowledge

# Acceptance Criteria:

@US187 @US189 @User @IS @Trill
Scenario: Record IS System Skills
Given I am a User
And I am logged into Trill
And I select Skills
When I record my IS Systems skills
And exit the application
And I am logged into Trill
And I select Skills
Then my IS Systems skills will displayed
