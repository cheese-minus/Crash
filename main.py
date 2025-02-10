import tkinter as tk
from strategy import BettingStrategy
from tracker import BetTracker
from gui import CrashGameApp

def main():
    """Initialize and launch the crash game betting app."""
    tracker = BetTracker()  # Create an instance of the tracker
    strategy = BettingStrategy(tracker)  # Pass tracker to strategy

    # Initialize GUI with the strategy and tracker
    root = tk.Tk()
    app = CrashGameApp(root, strategy, tracker)

    root.mainloop()

if __name__ == "__main__":
    main()