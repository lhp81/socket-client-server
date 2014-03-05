Feature: An echo server
    Implement an echo server.

    Scenario Outline: Echo server that receives strings
        Given the string <input>
        When I send with echo_client
        Then I see <output>

    Examples:
        | input                                                             | output                                                            |
        | Besame. Besame mucho!                                             | Besame. Besame mucho!                                             |
        | 1234567890987654321234567890-=-0                                  | 1234567890987654321234567890-=-0                                  |
        | Twas brillig and the slithy toves did gyre and gible in the wabe. | Twas brillig and the slithy toves did gyre and gible in the wabe. |