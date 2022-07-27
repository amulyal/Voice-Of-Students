Scenario: Orientation Feedback
    Given As a Student
    And upon completion of my college induction program
    When I receive an email with survey link
    Then I should be able to answer the survey where I can share my experience about the college 

Scenario: Admission Feedback
    Given As a Student 
    And upon completion of my admission process 
    When I receive an email with survey link 
    Then I should be able to answer the survey where I can provide feedback about admission and on-boarding

Scenario: Educator Feedback
    Given As a Student
    And I have 3 months of completion in college
    When I receive an email with survey link
    Then I should be able to answer the survey where I can provide opinion about educator

Scenario: Semester Educator Feedback
    Given As a Student
    And I have completed one semester in college
    But I have not graduated
    When I receive an email with survey link
    Then I should be able to answer the survey where I can provide opinion about Educator 

Scenario: Activities Feedback
    Given As a student
    When I receive an email with survey link 
    Then I should be able to answer the survey where I can provide opinion about Extra Curriculum, Annual Function, Events etc.

Scenario: Graduation Feedback
    Given As a student
    And I have completed 8 semesters in college
    When I receive an email with survey link 
    Then I should be able to answer the survey where I can provide opinion about College Management and Governanace

Scenario: Parent Feedback
    Given As a parent 
    And upon completion of one year of their child's study
    When I receive an email with survey link
    Then I should be able to answer the survey where I can provide opinion about College Curriculum, Coaching, Governance and Student Performance
