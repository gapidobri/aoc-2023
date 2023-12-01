from re import findall

print(sum(int(n[0] + n[-1]) for n in (findall(r"\d", l) for l in open("input.txt"))))

dm = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def strtodig(l):
    for n, d in enumerate(dm, start=1):
        l = l.replace(d, d[0] + str(n) + d[-1])
    return l


print(
    sum(
        int(n[0] + n[-1])
        for n in (findall(r"\d", strtodig(l.strip())) for l in open("input.txt"))
    )
)
