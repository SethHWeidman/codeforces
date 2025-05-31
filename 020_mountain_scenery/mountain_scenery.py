'''
https://codeforces.com/problemset/problem/218/A
1,100 rate Codeforces problem that, embarassingly, took several tries to get
'''


def mountain_scenery(n: int, k: int, vertices: list[int]) -> list[int]:
    ks_chosen = []
    for i in range(1, 2 * n + 1 + 1, 2):
        if vertices[i - 1] < vertices[i] - 1 and vertices[i] - 1 > vertices[i + 1]:
            ks_chosen.append(i)
            if len(ks_chosen) == k:
                break
    for vertex in ks_chosen:
        vertices[vertex] -= 1
    return vertices


def solve():
    n, k = list(map(int, input().strip().split()))
    vertices = list(map(int, input().strip().split()))
    updated_vertices = mountain_scenery(n, k, vertices)
    print(" ".join([str(x) for x in updated_vertices]))


if __name__ == "__main__":
    solve()
