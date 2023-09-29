import matplotlib.pyplot as plt

# قائمة بحجم البيانات (X-axis)
data_sizes = [10, 20, 30, 40, 50]

# قائمة بالدقة (Y-axis)
accuracy = [0.85, 0.88, 0.91, 0.92, 0.93]

# رسم منحنى التعلم
plt.plot(data_sizes, accuracy, marker='o', linestyle='-')
plt.xlabel(' Data size ')
plt.ylabel(' Accuracy ')
plt.title(' Learning curve ')
plt.grid(True)
plt.show()