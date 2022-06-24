from breezypythongui import EasyFrame
class TemperatureConversionDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.fahrenheitLabel=self.addLabel(text="Fahrenheit",sticky="W",
                                            row =0,column=0,columnspan=2)
        self.fahrenheitField=self.addFloatField(value=0.0,sticky="NSEW",
                                                  row=1,column=0,columnspan=2,precision=2)
        self.fahrenheitField.bind("<Return>", lambda event: self.convertToCelsius())
        self.celsiusLabel=self.addLabel(text="Celsius",sticky="W",
                                                 row=0,column=2,columnspan=2)
        self.celsiusField=self.addFloatField(value=0.0,sticky="NSEW",
                                                 row=1,column=2,columnspan=2,precision=2)
        self.celsiusField.bind("<Return>", lambda event: self.convertToFahrenheit())

    def convertToCelsius(self):
        celsius=(self.fahrenheitField.getNumber()-32)*(5/9)
        self.celsiusField.setNumber(celsius)

    def convertToFahrenheit(self):
        fahrenheit =self.celsiusField.getNumber()*(9/5) + 32
        self.fahrenheitField.setNumber(fahrenheit)

def main():TemperatureConversionDemo().mainloop()
if __name__ =="__main__":
    main()


