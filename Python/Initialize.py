class Probability:
    def __init__(self, list_of_values, list_of_probabilities = None, function = None):
        if len(list_of_values) == 0:
            raise ValueError("The list of values cannot be empty")
        if len(list_of_values) != len(set(list_of_values)):
            raise ValueError("The list of values cannot have duplicates")
        if list_of_probabilities == None and function == None:
            raise ValueError("You must give either a list of probabilities or a function")
        elif list_of_probabilities != None and function != None:
            if self.check_pf(list_of_values, list_of_probabilities, function):
                self.values = list_of_values
                self.probabilities = list_of_probabilities
                self.function = function

        elif list_of_probabilities != None:
            if len(list_of_values) != len(list_of_probabilities):
                raise ValueError("The list of values and the list of probabilities must be the same length")
            if self.check_p(list_of_probabilities):
                self.values = list_of_values
                self.probabilities = list_of_probabilities
                self.function = lambda x: list_of_probabilities[list_of_values.index(x)]
            else:
                raise ValueError("The probabilities must add up to 1 and be non-negative")
        elif function != None:
            if self.check_f(list_of_values, function):
                self.values = list_of_values
                self.probabilities = [function(x) for x in list_of_values]
                self.function = function
            else:
                raise ValueError("The function must give a valid probability distribution")
            
    
    def check_p(self, list_of_probabilities):
        if abs(sum(list_of_probabilities) - 1) > 1e-6:
            return False
        for x in list_of_probabilities:
            if x < 0:
                return False
        return True
    
    def check_f(self, list_of_values, function):
        for x in list_of_values:
            if function(x) < 0:
                return False
        if abs(sum([function(x) for x in list_of_values]) - 1) > 1e-6:
            return False
        return True
    
    def check_pf(self, list_of_values, list_of_probabilities, function):
        if abs(sum(list_of_probabilities) - 1) > 1e-6:
            return False
        for x in list_of_probabilities:
            if x < 0:
                return False
        for i in range(len(list_of_values)):
            if function(list_of_values[i]) != list_of_probabilities[i]:
                return False
        return True
    
    def check_subset(self, subset):
        for x in subset:
            if x not in self.values:
                return False
        return True
    
    def check_invariant(self, Invariant):
        for x in self.values:
            if not Invariant(x):
                return False
        return True

    def Event(self, subset = None, Invariant = None):
        if subset == None and Invariant == None:
            raise ValueError("You must give either a subset or an invariant")
        if subset != None and Invariant != None:
            raise ValueError("You must give either a subset or an invariant, not both")
        if subset != None:
            if self.check_subset(subset):
                return sum([self.probabilities[(self.values).index(i)] for i in subset])
            else:
                raise ValueError("The subset must be a subset of the values")
        if Invariant != None:
            if self.check_invariant(Invariant):
                return sum([function(i) for i in self.values if Invariant(i)])
            else:
                raise ValueError("The invariant must be a function that takes a value and returns a boolean")

    
    def conditioning(self, subset = None, Invariant = None):
        if subset == None and Invariant == None:
            raise ValueError("You must give either a subset or an invariant")
        if subset != None and Invariant != None:
            raise ValueError("You must give either a subset or an invariant, not both")
        if subset != None:
            if self.check_subset(subset):
                return Probability(subset, [self.function(i)/self.Event(subset) for i in subset])
            else:
                raise ValueError("The subset must be a subset of the values")
        if Invariant != None:
            if self.check_invariant(Invariant):
                return Probability(subset, [self.function(i)/self.Event(Invariant = Invariant) for i in subset])
            else:
                raise ValueError("The invariant must be a function that takes a value and returns a boolean")



            
