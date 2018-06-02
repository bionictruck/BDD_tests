# -- FILE: features/my_courses.feature
Feature: Login to Coursera and view My Courses

  Scenario: I login and view My Courses
    Given I am on coursera.org
    When I click the Log In link
    And I enter my email into the Email field
    And I enter my password into the Password field
    And I click the Log In button
    Then I am shown My Courses

Scenario: I view and verify my Inactive Courses
    Given I am on coursera.org
    When I click Inactive Courses
    Then I see Constitutional Law

Scenario: I view and verify my Completed Courses
    Given I am on coursera.org
    When I click Completed Courses
    Then I see Programming for Everybody (Python)

Scenario: I view and verify my Accoomplishments
    Given I am on coursera.org
    When I click Accomplishments
    Then I see ID Verification

Scenario: I view and verify my Updates
    Given I am on coursera.org
    WHen I click Updates
    Then I see Free trials offered now

Scenario: I view and verify my Learning Paths
    Given I am on coursera.org
    When I click Learning Paths
    Then I see Looking for the perfect course? We're here to help.