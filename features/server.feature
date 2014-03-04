Feature: An echo server
    Implement an echo server that receives and echos back messages. This sort
    of thing would be very dangerous for Narcissus, so if you see him, don't
    let him anywher near this.

    Scenario Outline: Echo server that receives strings
        Given the string <input>
        When I send it with the echo_client
        Then I see <output>

    Examples:
        | input                                                             | output                                                            |
        | Besame. Besame mucho!                                             | Besame. Besame mucho!                                             |
        | 1234567890987654321234567890-=-0                                  | 1234567890987654321234567890-=-0                                  |
        | Twas brillig and the slithy toves did gyre and gible in the wabe. | Twas brillig and the slithy toves did gyre and gible in the wabe. |