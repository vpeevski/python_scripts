import sys
def isNumber(n, min = -1, max = sys.maxsize):
    print("isNumberInInterval called with:", n)
    try:
        val = int(n)
        return min <= val and val <= max
    except ValueError:
        return False


def isNumberEx(n, min=-1, max=sys.maxsize):
    if isNumber(n, min, max):
        sys.exit(0)
    sys.exit(1)