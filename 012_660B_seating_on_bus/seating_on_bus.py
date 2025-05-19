import collections


def get_off_bus_order(n: int, m: int) -> list[int]:

    # The LLM suggested a more mathematical solution:

    # order: list[str] = []

    # # 1 … 2 n  →  window seats (left-window, right-window, row-by-row)
    # # 2 n+1 … 4 n  →  non-window seats (left-non, right-non row-by-row)

    # for row in range(1, n + 1):
    #     # Compute the four seat indices for this row
    #     lw = 2 * (row - 1) + 1  # left window
    #     rw = 2 * (row - 1) + 2  # right window
    #     ln = 2 * n + 2 * (row - 1) + 1  # left non-window
    #     rn = 2 * n + 2 * (row - 1) + 2  # right non-window

    #     # Passengers leave in the order: LN, LW, RN, RW
    #     for seat in (ln, lw, rn, rw):
    #         if seat <= m:  # only append if someone actually boarded
    #             order.append(seat)

    #     if len(order) == m:  # early exit if we've listed everyone
    #         break

    # return order

    left_window_deque = collections.deque(maxlen=n)
    left_aisle_deque = collections.deque(maxlen=n)
    right_window_deque = collections.deque(maxlen=n)
    right_aisle_deque = collections.deque(maxlen=n)
    for i in range(1, m + 1):
        if i <= 2 * n:  # we are still adding to window seats
            if i % 2 == 1:
                left_window_deque.append(i)
            else:
                right_window_deque.append(i)
        else:
            if i % 2 == 1:
                left_aisle_deque.append(i)
            else:
                right_aisle_deque.append(i)

    disembarkation_order = []
    i = 0
    while True:
        if not len(left_aisle_deque) and len(left_window_deque):
            disembarkation_order.append(left_window_deque.popleft())
            i += 1
            if i >= m:
                break
        else:
            disembarkation_order.append(left_aisle_deque.popleft())
            i += 1
            if i >= m:
                break
            disembarkation_order.append(left_window_deque.popleft())
            i += 1
            if i >= m:
                break

        if not len(right_aisle_deque) and len(right_window_deque):
            disembarkation_order.append(right_window_deque.popleft())
            i += 1
            if i >= m:
                break
        else:
            disembarkation_order.append(right_aisle_deque.popleft())
            i += 1
            if i >= m:
                break
            disembarkation_order.append(right_window_deque.popleft())
            i += 1
            if i >= m:
                break

    return disembarkation_order


def solve():
    m, n = map(int, input().split())
    disembarkation_order = get_off_bus_order(m, n)
    # The LLM suggested:
    #
    # print(" ".join(map(str, disembarkation_order)))
    s = ""
    for person in disembarkation_order:
        s = s + str(person) + " "
    print(s)


if __name__ == "__main__":
    solve()
