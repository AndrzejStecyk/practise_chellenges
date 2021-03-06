"""
https://edabit.com/challenge/67nLEyXHRZMpBjnbZ

* No description.
* Guess the code from test cases.

running_athlete(["run", "jump", "run", "jump", "run"], "_|_|_") ➞ "_|_|_"
running_athlete(["run", "jump", "run", "run", "run"], "_|_|_") ➞ "_|_/_"
running_athlete(["jump", "jump", "jump", "jump", "jump"], "_|_|_") ➞ "x|x|x"
running_athlete(["run", "run", "run", "run", "run"], "_|_|_") ➞ "_/_/_"
"""


def running_athlete(act, txt):
    rules = {'run': ['_', '/'],
             'jump': ['|', 'x']}

    result = str()
    for move, obstacle in zip(act, txt):
        if rules[move][0] == obstacle:
            result += rules[move][0]
        else:
            result += rules[move][1]

    return result


if __name__ == '__main__':
    print(running_athlete(["run", "jump", "run", "jump", "run"], "_|_|_"))  # => "_|_|_"
    print(running_athlete(["run", "jump", "run", "run", "run"], "_|_|_"))  # => "_|_/_"
    print(running_athlete(["run", "run", "run", "run", "run"], "_|_|_"))  # => "_/_/_"
    print(running_athlete(["jump", "jump", "jump", "jump", "jump"], "_|_|_"))  # => "x|x|x"
    print(running_athlete(["jump", "run", "jump", "run", "jump"], "_|_|_"))  # => "x/x/x"
    print(running_athlete(["run", "run", "run", "run", "run", "run", "run", "run", "run", "run"],
                          "||||||||||"))  # => "//////////"
    print(running_athlete(["jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump", "jump"],
                          "__________"))  # => "xxxxxxxxxx"
