
import matplotlib.pyplot as plt

def show_chart(data):
    plt.plot(data)
    plt.title("Performance Trend")
    plt.xlabel("Matches")
    plt.ylabel("Score")
    plt.show()
