def cableway(r: int, g: int, b: int) -> int:
    """
    Given:
        * Counts of students r, g, b who ride red, green, and blue cars respectively
        * Each car holds up to 2 people
        * Cars arrive every minute in an R, G, B cycle starting with red at t = 0
        * Travel time is 30 minutes

    Return the time when the last student arrives at the top.
    """
    # Note: an LLM helped me realize that e.g. `num_red_cars = (r + 1) // 2` would have
    # been cleaner...
    num_red_cars = max((r - 1) // 2 + 1, 0)
    num_green_cars = max((g - 1) // 2 + 1, 0)
    num_blue_cars = max((b - 1) // 2 + 1, 0)

    # ...followed by:
    # arrival_red = 30 + (num_red - 1) * 3 if r > 0 else 0
    # # (same for green and blue)
    # return max(arrival_red, arrival_green, arrival_blue)
    if num_blue_cars >= max(num_red_cars, num_green_cars):
        return 30 + (num_blue_cars - 1) * 3 + 2
    elif num_green_cars >= num_red_cars:
        return 30 + (num_green_cars - 1) * 3 + 1
    else:
        return 30 + (num_red_cars - 1) * 3


def solve():
    """
    An LLM helped with this
    """
    r, g, b = map(int, input().split())
    print(cableway(r, g, b))


if __name__ == "__main__":
    solve()
