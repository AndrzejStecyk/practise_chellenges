from unittest import TestCase
from encode_morse import encode_morse


class Test(TestCase):
    def test_encode_morse(self):
        self.assertEqual(encode_morse("EDABBIT CHALLENGE"),
                          ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .", "self 1")
        self.assertEqual(encode_morse("HELP ME !"), ".... . .-.. .--.   -- .   -.-.--", "self 2")
        self.assertEqual(encode_morse("CHALLENGE"), "-.-. .... .- .-.. .-.. . -. --. .", "self 3")
        self.assertEqual(
            encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."),
            ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-",
            "self 4")
        self.assertEqual(encode_morse("did you got my mail ?"),
                          "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..", "self 5")
        self.assertEqual(encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C"),
                          "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.",
                          "self 6")
