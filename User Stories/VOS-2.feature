Scenario: Address Concerns
    Given As a Principal 
    When I need to be able to capture all net promoter score detractors as complaints
    Then I can to contact the student or parent to address their concerns

Scenario: Analyse Response
    Given As a Principal
    When I need to be able to view the student response
    Then I should analyse feedback based on Department
    And Class
    And Semester

Scenario: Hierarchy for Survey Template
    Given As a Principal
    When event
    Then outcome

Scenario: Modify Survey Template
    Given As a Principal
    When I decide the hierarchy of the survey template is done
    Then I should be able to create, modify and delete Survey Template 

Scenario: Survey Reminders
    Given As a Principal
    When I do not receive response from student or parent
    And A week has been passed since the surbey has been sent
    Then I should be able to send automated reminder to complete feedback

Scenario: Bounced Email
    Given As a Principal
    When I receive a bounced email
    Then I should be able to send the survey via SMS to the student 

Scenario: Graphical Analysis
    Given As a Principal
    When I receive the feedback responses
    Then I should be able to view dashbaord with feedback response and NPS score in graphical format

Scenario: Status of Survey
    Given As a Principal
    When I sent the survey out for feedback
    Then I should be able to see the status of the survey response

Scenario: title
    Given As a Principal
    When include and exclude ??
    Then outcome

Scenario: Survey Specification 
    Given As a Principal
    When I create the survey
    Then I should be able to include questions, images, emojis and emoticons

Scenario: Raise Ticket
    Given As a Principal
    When I receive a negative feedback
    Then I should be able to raise a ticket and send alert on the feedback obtained to the department and staff

Scenario: Track Ticket
    Given As a Principal
    When I have raised a ticket
    Then I should be able to track the ticket as open/ escalate/ resolved/ closed/ invalid

Scenario: Resolved Ticket
    Given As a Principal
    When I resolve the ticket successfully
    Then I should be able to send an email to the student or parent 