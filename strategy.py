import numpy as np
from tracker import BetTracker

class BettingStrategy:
    def _init_(self, tracker):
        """Initialize the strategy with a tracker instance."""
        if not isinstance(tracker, BetTracker):
            raise TypeError("Expected tracker to be an instance of BetTracker")
        
        self.tracker = tracker
        self.base_stake = 0.00000010  # Starting stake (ETH)
        self.multiplier = 2.0  # Default multiplier
        self.profit_lock = 0.2  # 20% of winnings locked
        self.current_stake = self.base_stake

    def next_bet(self, last_result: bool):
        """
        Determines the next bet based on the last outcome.
        Uses NumPy for smarter stake adjustments.
        """
        win_rate = self.tracker.get_win_rate()
        loss_streak = self.tracker.get_loss_streak()
        total_profit = self.tracker.get_total_profit()

        # Adaptive risk management using NumPy
        risk_factor = np.clip(win_rate * 2 - loss_streak / 5, 0.5, 2.0)

        if last_result:
            self.current_stake = max(self.base_stake, self.current_stake * 0.5)
        else:
            self.current_stake *= risk_factor  # Adjust based on streaks

        return self.current_stake, self.multiplier