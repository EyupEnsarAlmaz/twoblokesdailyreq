from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Stock:
    symbol: str
    name: str
    price: float
    changes_percentage: float
    change: float
    day_low: float
    day_high: float
    year_high: float
    year_low: float
    market_cap: float
    price_avg50: float
    price_avg200: float
    exchange: str
    volume: int
    avg_volume: int
    open_price: float
    previous_close: float
    eps: float
    pe: float
    earnings_announcement: str
    shares_outstanding: int
    timestamp: int



    @property
    def pivot_point(self) -> float:
        """Calculate the pivot point using high, low, and close prices"""
        return round((self.day_high + self.day_low + self.previous_close) / 3)

    @property
    def support_2(self) -> float:
        """Calculate second support level"""
        return round(self.pivot_point - (self.day_high - self.day_low), 4)

    @property
    def support_1(self) -> float:
        """Calculate first support level"""
        return round((2 * self.pivot_point) - self.day_high, 4)

    @property
    def resistance_1(self) -> float:
        """Calculate first resistance level"""
        return round((2 * self.pivot_point) - self.day_low, 4)

    @property
    def resistance_2(self) -> float:
        """Calculate second resistance level"""
        return round(self.pivot_point + (self.day_high - self.day_low), 4)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            symbol=data['symbol'],
            name=data['name'],
            price=data['price'],
            changes_percentage=data['changesPercentage'],
            change=data['change'],
            day_low=data['dayLow'],
            day_high=data['dayHigh'],
            year_high=data['yearHigh'],
            year_low=data['yearLow'],
            market_cap=data['marketCap'],
            price_avg50=data['priceAvg50'],
            price_avg200=data['priceAvg200'],
            exchange=data['exchange'],
            volume=data['volume'],
            avg_volume=data['avgVolume'],
            open_price=data['open'],
            previous_close=data['previousClose'],
            eps=data['eps'],
            pe=data['pe'],
            earnings_announcement=data['earningsAnnouncement'],
            shares_outstanding=data['sharesOutstanding'],
            timestamp=data['timestamp']
        )

    def __str__(self):
        return f"{self.symbol:<8} {self.name:<30} ${self.price:>9.2f} {self.changes_percentage:>9.2f}%"


