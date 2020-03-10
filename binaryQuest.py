
class Binary(object):
    answer = " "

    def yes(answer):
        return "yes"
    
    def no(answer):
        return "no"
    
    def __init__(self, answer):
        answer = input()
        if (answer in ["Yes", "Yea", "Sure", "Yeah", "Indeed", "Ye"]):
            self.yes()
        if (answer in ["No", "Nah", "Nein", "Negative", "Negatory", "Nope"]):
            self.no()
            
            
