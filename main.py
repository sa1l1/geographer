import matplotlib.pyplot as plt

def plot_rectangle(bottom_left, top_right):
    x_bottom_left, y_bottom_left = bottom_left
    x_top_right, y_top_right = top_right

    width = x_top_right - x_bottom_left
    height = y_top_right - y_bottom_left

    plt.gca().add_patch(plt.Rectangle((x_bottom_left, y_bottom_left), width, height, color='red', alpha=0.3))

def main():
    # Enter the coordinates for the bottom-left point of the first rectangle
    bottom_left_1 = (2, 2)
    # Enter the coordinates for the top-right point of the first rectangle
    top_right_1 = (8, 6)

    # Enter the coordinates for the bottom-left point of the second rectangle
    bottom_left_2 = (4, 4)
    # Enter the coordinates for the top-right point of the second rectangle
    top_right_2 = (10, 8)

    plot_rectangle(bottom_left_1, top_right_1)
    plot_rectangle(bottom_left_2, top_right_2)

    x_min = min(bottom_left_1[0], bottom_left_2[0]) - 1
    x_max = max(top_right_1[0], top_right_2[0]) + 1
    y_min = min(bottom_left_1[1], bottom_left_2[1]) - 1
    y_max = max(top_right_1[1], top_right_2[1]) + 1

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Rectangle Plot')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
