# -- FILE: features/profile.feature
Feature: Login to Coursera and view my Profile

Scenario: I log in and view my Profile
	Given I am on coursera.org
	When I click the Log In link
    And I enter my email into the Email field
    And I enter my password into the Password field
    And I click the Log In button
    And I am on my profile page
    Then I can edit my profile

Scenario: I can change my name in my profile
	Given I am on my profile page
	When I enter a <name>
	And I click the Save button
	Then I can see my <name> has been saved
		| <name>      |
		| Jay Test    |
		| 12345 Test  |
		| !@#$%^ Test |