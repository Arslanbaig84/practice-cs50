

# Implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:
# __init__ should initialize a cookie jar with the given capacity. If capacity is negative int, though, __init__ should instead raise a ValueError.
# __str__ should return a str with 🍪. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If deposit + str > capacity, though, deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar. If withdraw < str, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar.


class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a postive integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n < 0 or (self._cookies + n) > self._capacity:
            raise ValueError("Exceeded cookie jar's capacity.")
        self._cookies += n

    def withdraw(self, n):
        if n < 0 or (self._cookies - n) < 0:
            raise ValueError("Not enough cookies in the jar.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


def main():
    jar = Jar(10)
#    print(jar)
    jar.deposit(7)
#    print(jar)
    jar.withdraw(5)
    print(jar)


if __name__ =="__main__":
    main()