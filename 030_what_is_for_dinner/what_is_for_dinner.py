def what_is_for_dinner(m: int, k: int, teeth_tuples: list[tuple[int]]) -> int:
    teeth_row_capacity = {x: None for x in list(range(1, m + 1))}

    for teeth_tuple in teeth_tuples:
        row_index, tooth_capacity = teeth_tuple[0], teeth_tuple[1]
        if teeth_row_capacity[row_index] == None:
            teeth_row_capacity[row_index] = tooth_capacity
        else:
            teeth_row_capacity[row_index] = min(
                teeth_row_capacity[row_index], tooth_capacity
            )

    total_crucian_capacity = sum(teeth_row_capacity.values())
    return min(k, total_crucian_capacity)


def solve():
    n, m, k = list(map(int, input().strip().split()))
    teeth_tuples = []
    for _ in range(n):
        tooth_tuple = tuple(map(int, input().strip().split()))
        teeth_tuples.append(tooth_tuple)

    print(what_is_for_dinner(m, k, teeth_tuples))


if __name__ == "__main__":
    solve()
