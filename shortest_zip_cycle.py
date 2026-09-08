import sys

s = input()
n = len(s)

def main():
    for i in range(len(s), 2, -1):
        if n // i * i == n:
            ns = s[:n//i] * i
            if ns == s:
                print(s[:n//i], i, sep="")
                return
    print(s)

main()

