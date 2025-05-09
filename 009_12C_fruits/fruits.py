'''
https://codeforces.com/problemset/problem/12/C
Solved in 16 mins on 5/7/2025
'''

import collections
import typing


def fruits(prices: list[int], fruits_list: list[str]) -> typing.Tuple[int]:
    counter_sorted = collections.Counter(fruits_list).most_common()

    # realized after the fact it would have been cleaner to use:
    # * `prices = sorted(prices)`
    # * `prices_reversed = sorted(prices, reverse=True)`
    prices_reversed = prices.copy()
    prices.sort()
    prices_reversed.sort(reverse=True)

    num_fruits = len(counter_sorted)

    # most to least
    fruits_sorted = [x[0] for x in counter_sorted]

    fruit_to_price_map_min = {
        fruit: price for fruit, price in zip(fruits_sorted, prices[:num_fruits])
    }
    fruit_to_price_map_max = {
        fruit: price for fruit, price in zip(fruits_sorted, prices_reversed[:num_fruits])
    }

    return sum(fruit_to_price_map_min[fruit] for fruit in fruits_list), sum(
        fruit_to_price_map_max[fruit] for fruit in fruits_list
    )


def solve():
    """
    An LLM helped with this
    """
    num_prices, num_fruits = map(int, input().split())
    prices = list(map(int, input().split()))
    fruits_list = [input().strip() for _ in range(num_fruits)]
    min_price, max_price = fruits(prices, fruits_list)
    print(min_price, max_price)


if __name__ == "__main__":
    solve()
