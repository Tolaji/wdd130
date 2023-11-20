class  FuelEfficiency:
    def __init__(self, start, end, gallons):
        self.start = start
        self.end = end
        self.gallons = gallons
        
    def miles_per_gallon(self):        
      return (self.end - self.start)/self.gallons
    
    def lp100k_from_mpg(self, mpg):  
      return 235.215/mpg
    
def main():
    
    start = float(input('Enter starting odometer value in miles: '))
    end = float(input('Enter ending odometer value in miles: '))
    gallons = float(input('Enter amount of fuel in gallons: '))
    
    calculator = FuelEfficiency(start, end, gallons)
    
    mpg = calculator.miles_per_gallon()
    lp100k = calculator.lp100k_from_mpg(mpg)
    
    print(f"Fuel Efficiency in Miles per Gallon: {mpg:.2f} mpg")
    print(f"Fuel Efficiency in Liters per 100 Kilometers: {lp100k:.2f} lp100k")
        

main()
    
    