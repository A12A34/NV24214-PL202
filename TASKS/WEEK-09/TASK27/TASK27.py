import matplotlib.pyplot as plt


x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


def linear_regression(x_values, y_values):
    count = len(x_values)
    x_mean = sum(x_values) / count
    y_mean = sum(y_values) / count

    numerator = sum(
        (x_item - x_mean) * (y_item - y_mean)
        for x_item, y_item in zip(x_values, y_values)
    )
    denominator = sum((x_item - x_mean) ** 2 for x_item in x_values)

    slope = numerator / denominator
    intercept = y_mean - (slope * x_mean)
    return slope, intercept


slope, intercept = linear_regression(x, y)
predicted_speed = slope * 10 + intercept

print(f"Predicted speed for a 10-year-old car: {predicted_speed:.2f}")

plt.scatter(x, y, color="blue", label="Car data")
plt.plot(
    x,
    [slope * age + intercept for age in x],
    color="red",
    label="Regression line",
)
plt.xlabel("Car age")
plt.ylabel("Speed")
plt.title("Linear Regression")
plt.legend()
plt.show()
