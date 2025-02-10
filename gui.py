import tkinter as tk
from tkinter import messagebox
from graph import RealTimeGraph

class CrashGameApp:
    def _init_(self, root, strategy, tracker):
        self.root = root
        self.strategy = strategy
        self.tracker = tracker

        self.root.title("Crash Game Bot")
        self.root.geometry("400x300")

        # Current Stake & Multiplier Display
        self.stake_label = tk.Label(root, text="Stake: 0.00000010 ETH")
        self.stake_label.pack(pady=5)

        self.multiplier_label = tk.Label(root, text="Multiplier: 2.0x")
        self.multiplier_label.pack(pady=5)

        # Bet Result Buttons
        self.win_button = tk.Button(root, text="Win", command=lambda: self.process_bet(True))
        self.win_button.pack(pady=5)

        self.lose_button = tk.Button(root, text="Lose", command=lambda: self.process_bet(False))
        self.lose_button.pack(pady=5)

        # Insights Button
        self.insights_button = tk.Button(root, text="View Insights", command=self.show_insights)
        self.insights_button.pack(pady=5)

        # Real-time Graph
        self.graph = RealTimeGraph()
        self.graph.start_plot()

    def process_bet(self, result):
        """Processes the bet and updates the GUI."""
        stake, multiplier = self.strategy.next_bet(result)
        self.stake_label.config(text=f"Stake: {stake:.8f} ETH")
        self.multiplier_label.config(text=f"Multiplier: {multiplier:.2f}x")
        self.graph.update_graph(self.tracker.get_total_profit())

    def show_insights(self):
        """Displays historical performance insights."""
        win_rate = self.tracker.get_win_rate()
        loss_streak = self.tracker.get_loss_streak()
        total_profit = self.tracker.get_total_profit()
        messagebox.showinfo("Insights", f"Win Rate: {win_rate:.2%}\nLoss Streak: {loss_streak}\nTotal Profit: {total_profit:.8f} ETH")