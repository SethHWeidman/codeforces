def the_time(time: str, n_minutes: int) -> str:

    hour, minute = time.split(":")

    added_hours, new_minutes = divmod(int(minute) + n_minutes, 60)

    new_hours = (int(hour) + added_hours) % 24

    return f"{str(new_hours).zfill(2)}:{str(new_minutes).zfill(2)}"


def solve():
    time = input().strip()
    n_minutes = int(input())
    print(the_time(time, n_minutes))


if __name__ == "__main__":
    solve()
