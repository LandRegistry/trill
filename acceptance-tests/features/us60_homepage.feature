Feature: Home Page

# Acceptance Criteria
# - First screen displayed to users will be the Home Page screen

@US60 @USHome_Page1
Scenario:  Select Skills on Home Page (Not logged In)

Given I am on the Home Page
And I am not logged in
And I select Skills
When I am prompted to login
Then I login into Trill
And I will go to Skills page


@US60 @USHome_Page1
Scenario:  Select Resource on Home Page

Given I am on the Home Page
And I am not logged in
And I select Resource
When I am prompted to login
Then I login into Trill
And I will go to Resource page

@US60 @USHome_Page1
Scenario:  Select Record Skills on Home Page

Given I am on the Home Page
And I am not logged in
And I select Record Skills
When I am prompted to login
Then I login into Trill
And I will go to Skills page

@US60 @USHome_Page2
Scenario:  Select Skills on Home Page (Logged In)

Given I am on the Home Page
And I am logged into Trill
When I select Skills
Then I will go to Skills page


@US60 @USHome_Page2
Scenario:  Select Resource on Home Page

Given I am on the Home Page
And I am logged into Trill
When I select Resource
Then I will go to Resource page

@US60 @USHome_Page2
Scenario:  Select Record Skills on Home Page

Given I am on the Home Page
And I am logged into Trill
When I select Record Skills
Then I will go to Skills page
