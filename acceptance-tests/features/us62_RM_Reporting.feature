Feature: Run Resource Reports

@US62 @Manager @Report @Trill
Scenario: Search for Skills and Knowledge
Given I am a Manager
And I am logged into Trill
And I select a Skill known to be held as Expert
And I select a Skill known to be held as Proficient
And I select Knowledge known to be held as Basic
And I select the reporting tool
When I generate a report expecting results
Then I will see a results for the selected Expert Skill
And I will see a results for the selected Proficient Skill
And I will see a results for the selected Basic Knowledge

@US62 @Manager @Report @Trill
Scenario: No Results Search
Given I am a Manager
And I am logged into Trill
And I select Skill known to be held as None
And I select Knowledge known to be held as None
And I select the reporting tool
When I generate a report expecting no results
Then I will see a message stating that no results were found for the search
