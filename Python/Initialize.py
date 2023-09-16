class Probability:
    def __init__(self, list_of_values, list_of_probabilities = None, function = None):
        if len(list_of_values) == 0:
            raise ValueError("The list of values cannot be empty")
        if len(list_of_values) != len(set(list_of_values)):
            raise ValueError("The list of values cannot have duplicates")
        if list_of_probabilities == None and function == None:
            raise ValueError("You must give either a list of probabilities or a function")
        if list_of_probabilities != None and function != None:
            if self.check_pf(list_of_values, list_of_probabilities, function):
                self.values = list_of_values
                self.probabilities = list_of_probabilities
                self.function = function

        if list_of_probabilities != None:
            if len(list_of_values) != len(list_of_probabilities):
                raise ValueError("The list of values and the list of probabilities must be the same length")
            if self.check_p(list_of_probabilities):
                self.values = list_of_values
                self.probabilities = list_of_probabilities
                self.function = lambda x: list_of_probabilities[list_of_values.index(x)]
            else:
                raise ValueError("The probabilities must add up to 1 and be non-negative")
        if function != None:
            if self.check_f(list_of_values, function):
                self.values = list_of_values
                self.probabilities = [function(x) for x in list_of_values]
                self.function = function
            else:
                raise ValueError("The function must give a valid probability distribution")
            
    
    def check_p(self, list_of_probabilities):
        if sum(list_of_probabilities) != 1:
            return False
        for x in list_of_probabilities:
            if x < 0:
                return False
        return True
    
    def check_f(self, list_of_values, function):
        for x in list_of_values:
            if function(x) < 0:
                return False
        if sum([function(x) for x in list_of_values]) != 1:
            return False
        return True
    
    def check_pf(self, list_of_values, list_of_probabilities, function):
        if sum(list_of_probabilities) != 1:
            return False
        for x in list_of_probabilities:
            if x < 0:
                return False
        for i in range(len(list_of_values)):
            if function(list_of_values[i]) != list_of_probabilities[i]:
                return False
        return True
    
    
    

    


