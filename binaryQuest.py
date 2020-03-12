
class Binary(object):


    which = bool(False)
    
    def __init__(self):
        self.answer = input("Yes/No?: ")
        if (self.answer in ["Yes", "yes", "YEs", "YES", "Yea", "yea", "Sure", "sure", "Yeah", "yeah", "Indeed", "indeed", "Ye", "ye"]):
            Binary.which = True
        if (self.answer in ["No", "NO", "no", "Nah", "nah", "Nein", "nein", "Negative", "negative", "Negatory", "negatory", "Nope", "nope"]):
            Binary.which = False
            
        
