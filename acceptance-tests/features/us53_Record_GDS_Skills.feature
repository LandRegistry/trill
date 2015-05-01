Feature: Record GDS Skills
#US53 - As a Service Desk user I want to be able to add/edit my skills so that I can display my skills to other people.
# Acceptance criteria
# Only one option can be chosen for each skill.
# Only one option MUST be selected for each skill
# - Each option must be saved after each click
# - All options can be updated
# - All skills must default to None when user logs in for the first time or when no skill options have been entered
# - The Skill Screen must display any previously saved skills

# The skills displayed must have the following options
# - Proficient and Confidence levels are displayed against each GDS skill
# - Proficient level = None/ Basic / Proficient / Expert is displayed
# - Confidence level = None/ Low / Medium / High

# - Each option must be saved after each click
# - Default for both proficient and confidence must be None for each GDS skill
# -  An expanded explanation of what each level means can be displayed if needed  (see Richard for wording of each level)

@US53 @User @GDS @Trill @TrillRegress
Scenario: Record GDS Skills
Given I am a User
And I am logged into Trill
When I record my skills
Then my skills will be recorded

@US53 @User @GDS @Trill
Scenario: Record GDS Skills
Given I am a User
And I am logged into Trill
When I record my skills
And exit the application
and I am logged into Trill
Then my skills will displayed
