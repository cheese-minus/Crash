import matplotlib.pyplot as plt
import matplotlib.animation as animation

class RealTimeGraph:
    def _init_(self):
        self.profit_history = [0]  # Track bankroll over time
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.profit_history, label="Bankroll")
        self.ax.set_title("Bankroll Over Time")
        self.ax.set_xlabel("Bets")
        self.ax.set_ylabel("Profit (ETH)")
        self.ax.legend()

    def update_graph(self, profit):
        """Updates graph with new profit value."""
        self.profit_history.append(profit)
        self.line.set_ydata(self.profit_history)
        self.line.set_xdata(range(len(self.profit_history)))
        self.ax.relim()
        self.ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)

    def start_plot(self):
        """Shows the live updating graph in a separate window."""
        plt.ion()  # Interactive mode ON
        plt.show()