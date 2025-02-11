class Currency:
    def __init__(self, symbol, high, low, close):
        self.symbol = symbol
        self.high = high
        self.low = low
        self.close = close
        self._calculate_levels()
    
    def _calculate_levels(self):
        # Calculate Pivot Point
        self.pivot = (self.high + self.low + self.close) / 3
        # Calculate Support and Resistance levels
        self.resistance_2 = self.pivot + (self.high - self.low)
        self.resistance_1 = (2 * self.pivot) - self.low
        self.support_1 = (2 * self.pivot) - self.high
        self.support_2 = self.pivot - (self.high - self.low)
    
    def __str__(self):
        return (f"{self.symbol:<8} | R2: {self.resistance_2:.5f} | "
                f"R1: {self.resistance_1:.5f} | P: {self.pivot:.5f} | "
                f"S1: {self.support_1:.5f} | S2: {self.support_2:.5f}") 