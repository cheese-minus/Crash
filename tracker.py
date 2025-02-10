class BetTracker:
    def _init_(self):
        self.history = []  # Stores win/loss history
        self.total_profit = 0.0
        self.win_count = 0
        self.loss_count = 0

    def record_bet(self, stake, multiplier, won):
        """Records the outcome of a bet."""
        if won:
            profit = stake * (multiplier - 1)
            self.total_profit += profit
            self.win_count += 1
        else:
            self.total_profit -= stake
            self.loss_count += 1

        self.history.append((stake, multiplier, won))

    def get_win_rate(self):
        """Returns the win rate as a percentage."""
        total_bets = self.win_count + self.loss_count
        return self.win_count / total_bets if total_bets > 0 else 0.0

    def get_loss_streak(self):
        """Returns the current loss streak."""
        streak = 0
        for bet in reversed(self.history):
            if bet[2]:  # If win, break the streak
                break
            streak += 1
        return streak

    def get_total_profit(self):
        """Returns total profit."""
        return self.total_profit