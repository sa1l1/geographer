import matplotlib.pyplot as plt

def plot_rectangle(bottom_left, top_right):
    x_bottom_left, y_bottom_left = bottom_left
    x_top_right, y_top_right = top_right

    width = x_top_right - x_bottom_left
    height = y_top_right - y_bottom_left

    plt.gca().add_patch(plt.Rectangle((x_bottom_left, y_bottom_left), width, height, color='blue', alpha=0.3))
    plt.xlim(x_bottom_left - 1, x_top_right + 1)
    plt.ylim(y_bottom_left - 1, y_top_right + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Rectangle Plot')
    plt.grid()
    plt.show()

def main():
    # Enter the coordinates for the bottom-left point
    bottom_left = (2, 2)

    # Enter the coordinates for the top-right point
    top_right = (8, 6)

    plot_rectangle(bottom_left, top_right)

if __name__ == "__main__":
    main()
