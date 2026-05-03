import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

absences = np.array([1, 0, 7, 4, 9])

colors = ["#fde4f2", "#f9cee7", "#f4b8da", "#eea1cd", "#e68bbe"]

plt.figure(figsize=(9, 6))
bars = plt.bar(days, absences, color=colors, edgecolor="#333", linewidth=1.2)

plt.title("Weekly Attendance (Absences)", fontsize=16, fontweight="bold", color="#e68bbe")
plt.xlabel("Day", fontsize=12, color="#333")
plt.ylabel("Number of Absences", fontsize=12, color="#333")
plt.grid(axis="y", linestyle="--", alpha=0.5, color="#f4b8da")

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, str(height),
             ha='center', va='bottom', fontsize=11, color="#333")

plt.gca().set_facecolor("white")
plt.gcf().patch.set_facecolor("white")

plt.tight_layout()
plt.savefig("attendance_chart.png", dpi=120)
plt.close()
