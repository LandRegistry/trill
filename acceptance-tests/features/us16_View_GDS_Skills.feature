@US16  @User @Trill


Feature: View GDS Skills

#The screen should display the user’s name (first name - surname) and their role
Scenario: View Name and Role
Given I am a User
And I have a Role
When I login into Trill
Then I should go to my Trill homepage
And I should see my first name
And I should see my surname
And I should see my role

Given I am a User
And I do not have a Role
When I login into Trill
Then I should go to my Trill homepage
And I should see my first name
And I should see my surname
And I should not see my role


#The screen should display a title for the GDS skills section (the IS skills section will be added later)
Scenario: View GDS Skills Title
Given I am a User
And I have a Role
When I login into Trill
Then I should go to my Trill homepage
And I should see my GDS Skills Title

Scenario: No GDS Skills Title
Given I am a User
And I do not have a Role
When I login into Trill
Then I should go to my Trill homepage
And I should not see my GDS Skills Title


#The 3 skill groups relevant to the Service Desk should be displayed in boxes one on top of the other
Scenario: View Skill Boxes
Given I am a User
And I have a Role
And I have Skills
When I login into Trill
Then I should go to my Trill homepage
And I should see my relevant GDS Skill groups


#Clicking a skill group box should expand a list of all the skills in that group
Scenario: Expand Skill Boxes
Given I am on my Trill homepage
When I click on a GDS skill group
Then the skill group should expand
And I should see the additional skill group information relevant to my role


#Clicking an expanded skill group box should collapse it
Scenario: Collapse Skill Boxes
Given I am on my Trill homepage
When I click on an expanded GDS skill group
Then the skill group should collapse
And I should not see the additional skill group information relevant to my role
