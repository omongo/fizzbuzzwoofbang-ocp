import rules

class FizzBuzzWoofBangFactory:
    def create(self):
        return FizzBuzzWoofBang((rules.Fizz(), rules.Buzz(), rules.Woof(), rules.Bang()))

class FizzBuzzWoofBang:
    def __init__(self, rules):
        self._rules = rules
    def say(self, number):
        word = ''
        for rule in self._rules:
            word += rule.syllable * rule.is_valid(number)
        return word or str(number)

