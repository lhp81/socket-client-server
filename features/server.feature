Feature: Send/recieve data
    As a client
    I want to send a message to my server
    So it will be displayed and sent back to me

    Scenario: Receive data
    Given a message <message>
    When I send it to the server
    Then I see <output>

    | message | output |
    | hi      | hi     |
    | (^_^)   | (^_^)  |
    | 112358  | 112358 |