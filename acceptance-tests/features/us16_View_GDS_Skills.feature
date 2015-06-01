Feature: View GDS Skills

#a user consists of first name, surname, role, skills, email and password
@US16 @Name @Role @Trill @TrillRegress
Scenario: View Name and Role
Given I am a User
And I am on the Home Page
And I select Login
And I login into Trill
And I am on my Home Page
When I select Skills
Then I will go to Skills Page
And I can see my first name
And I can see my surname
And I can see my role

#This test has been considered but cannot be performed due to database restrictions
#@US16 @Name @Role @Tril
#Scenario: View Name and No Role
##Given I am a User
#And I do not have a Role
#When I login into Trill
#Then I will go to my Trill homepage
#And I can see my first name
#And I can see my surname
#And I cannot see my role

# The screen should display a title for the GDS skills section (the IS skills section will be added later)
@US16 @GDSskills @Trill
Scenario: View GDS Skills Title
Given I am a User
And I am logged into Trill
And I am on my Home Page
When I select Skills
Then I can see my GDS Skills Title

#This test has been considered but cannot be performed due to database restrictions
#@US16 @GDSskills @Trill
#Scenario: No GDS Skills Title
#Given I am a User
#And I do not have a Role
#And I am logged into Trill
#When I am on my Trill homepage
#Then I cannot see my GDS Skills Title




# The 3 skill groups relevant to the Service Desk should be displayed in boxes one on top of the other
@US16 @GDSskills @Trill
Scenario: View GDS Skill Boxes
Given I am a User
And I am logged into Trill
And I am on my Home Page
When I select Skills
Then I can see my relevant GDS Skill groups


# Clicking a skill group box should expand a list of all the skills in that group
@US16 @GDSskills @Trill @TrillRegress
Scenario: Expand GDS Skill Boxes
Given I am a User
And I am logged into Trill
And I am on my Home Page
When I select Skills
And I click on a collapsed GDS skill group
Then I can see the additional skill group information relevant to my role

# Clicking an expanded skill group box should collapse it
#@US16 @GDSskills @Trill
#Scenario: Collapse GDS Skill Boxes
#Given I am a User
#And I am logged into Trill
#And I am on my Home Page
#When I select Skills
#And I click on an expanded GDS skill group
#Then the skill group will collapse
#And I will not see the additional skill group information relevant to my role

# All data/names/skills on the page should come from the database
# @US16 cover this behaviour

# A GOV.UK style theme should be applied
# Witness testing will cover this
