class Divisors:
    def __init__(self, number):
        self.number = number
        self.ele = [i for i in range(1, number+1)]
        self.possible_divisors = []
        self.divisors = []
        self.result = None
        
    def split(self):
        print("this is split")
        for i in self.ele:
            for x in self.ele:
                if i*x == self.number:
                    self.possible_divisors.append(i)
                    self.possible_divisors.append(x)
                    print(f"possible divisors: {self.possible_divisors}")

    def flite(self):
        print("this is flite")
        for i in self.possible_divisors:
            if i not in self.divisors:
                self.divisors.append(i)
                
    def sum(self):
        pass
        
    def result_num(self):
        print("this is result")
        self.split()
        self.flite()
        self.result = sum(self.divisors)
        print(f'sum is {self.result}')
    
        
if __name__ == '__main__':
    stop = False
    while stop == False:
        number = input("Enter number: ")
        number = int(number)
        result = Divisors(number).result_num()
        condition_ = input("contiune Y for yes N for No:...")
        condition_ = condition_.lower()
        if condition_ == 'y':
            stop = False
        elif condition_ == 'n':
            stop = True
        else:
            stop = True

                    

        
