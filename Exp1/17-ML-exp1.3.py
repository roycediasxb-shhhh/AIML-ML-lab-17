import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# 1. Simple Line Plot
# -------------------------
x = np.array([0, 1, 2, 3, 4, 5])
y = x**2

plt.figure(figsize=(6, 4))
plt.plot(x, y, color='blue', linestyle='--', marker='o', label='y = x^2')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------
# 2. Multiple Lines
# -------------------------
y2 = x**3

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='y = x^2')
plt.plot(x, y2, label='y = x^3', color='red')
plt.title("Multiple Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# -------------------------
# 3. Scatter Plot
# -------------------------
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
sizes = np.random.randint(20, 200, 50)
colors = np.random.rand(50)

plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, s=sizes, c=colors,
            alpha=0.6, cmap='viridis')
plt.title("Scatter Plot")
plt.colorbar(label='Color Scale')
plt.show()

# -------------------------
# 4. Bar Plot
# -------------------------
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='orange')
plt.title("Bar Plot")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# -------------------------
# 5. Horizontal Bar Plot
# -------------------------
plt.figure(figsize=(6, 4))
plt.barh(categories, values, color='green')
plt.title("Horizontal Bar Plot")
plt.xlabel("Values")
plt.ylabel("Category")
plt.show()

# -------------------------
# 6. Histogram
# -------------------------
data = np.random.randn(1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='purple',
         edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# 7. Pie Chart
# -------------------------
labels = ['A', 'B', 'C', 'D']
explode = (0.1, 0, 0, 0)

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart")
plt.show()

# -------------------------
# 8. Subplots
# -------------------------
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1, 'b-', label='sin(x)')
plt.title('Sine Wave')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y2, 'r--', label='cos(x)')
plt.title('Cosine Wave')
plt.legend()

plt.tight_layout()
plt.show()

# -------------------------
# 9. Customization
# -------------------------
plt.figure(figsize=(6, 4))
plt.plot(x, y1, color='magenta', linestyle='-.',
         linewidth=2, marker='s', markersize=5)
plt.title("Customized Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle=':', linewidth=1)
plt.show()

# -------------------------
# 10. Saving Plots
# -------------------------
plt.figure()
plt.plot(x, y1)
plt.title("Plot to be Saved")
plt.savefig("sine_wave_plot.png")
plt.close()

print("All basic Matplotlib plots executed successfully!")
