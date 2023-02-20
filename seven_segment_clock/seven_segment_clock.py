def hour(seconds: int, base_24: bool) -> int:
    """Compute the number of full hours since midnight.

    Parameters
    ----------
    seconds : int
        Number of seconds since midnight.
    base_24 : bool
        If True, return hours using a 24-hour based format.
        If False, return hours using a 12-hour based format.

    Returns
    -------
    int
        Number of full ours since midnight.
    """
    if base_24:
        return int(seconds / 60 / 60)
    return int(int(seconds / 60 / 60) % 12)


def minute(seconds: int) -> int:
    """Compute the number of minutes the past clock hour.

    Parameters
    ----------
    seconds : int
        Number of seconds since midnight.

    Returns
    -------
    int
        number of minutes the past clock hour
    """

    return int((seconds - int(seconds / 60 / 60) * 60 * 60) / 60)


def lamp(digit: str) -> list[int]:
    """Get list of segments to light up for a digit.

    Parameters
    ----------
    digit : str
        Digit for which we want a list of segments to light.

    Returns
    -------
    list[int]
        List of segments to light up.
    """
    digit_segments = {
        "0": [1, 1, 0, 1, 1, 1, 1],
        "1": [0, 1, 0, 0, 1, 0, 0],
        "2": [1, 1, 1, 0, 0, 1, 1],
        "3": [1, 1, 1, 0, 1, 1, 0],
        "4": [0, 1, 1, 1, 1, 0, 0],
        "5": [1, 0, 1, 1, 1, 1, 0],
        "6": [1, 0, 1, 1, 1, 1, 1],
        "7": [1, 1, 0, 0, 1, 0, 0],
        "8": [1, 1, 1, 1, 1, 1, 1],
        "9": [1, 1, 1, 1, 1, 1, 0],
    }
    return digit_segments[digit]


def showClock(seconds: int, base24: bool) -> list[list[int]]:
    """Get list of segment to light up for each digit.

    Parameters
    ----------
    seconds : int
        Number of seconds since midnight.
    base_24 : bool
        If True, return hours using a 24-hour based format.
        If False, return hours using a 12-hour based format.

    Returns
    -------
    list[list[int]]
        List of segments to light up for digits from left to right.
    """
    seconds = seconds % (60 * 60 * 24)
    hour_number = hour(seconds, base24)
    minute_number = minute(seconds)
    digits = f"{hour_number:02d}{minute_number:02d}"
    return [lamp(digit) for digit in digits]


def display_clock(segment_lists):
    """Just for fun."""
    digits = []
    for segment_list in segment_lists:
        digit = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for index, segment in enumerate(segment_list):
            if segment == 1:
                if index == 0:
                    digit[0][1] = "‾"
                if index == 1:
                    digit[0][2] = "|"
                if index == 2:
                    digit[1][1] = "―"
                if index == 3:
                    digit[0][0] = "|"
                if index == 4:
                    digit[2][2] = "|"
                if index == 5:
                    digit[2][1] = "_"
                if index == 6:
                    digit[2][0] = "|"
        digits.append(digit)
        if len(digits) == 2:
            digits.append([[" ", "·", " "], [" ", " ", " "], [" ", "·", " "]])

    for row in range(3):
        for digit in digits:
            print("".join(digit[row]), end="")
        print()


if __name__ == "__main__":
    clock = showClock(int(60 * 60 * 20), True)
    # print(clock)
    display_clock(clock)
