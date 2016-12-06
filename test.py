import imba
imba.install("requests")

print("abc".len())
print([False, False].any())
print([False, True].any())
print([1, 2, 3].sum())
print("12345".map(int).sum())
print([1, 2, 3, 4].take(2))
print([1, 2, 3, 4].drop(2))

print({1: "a", 2: "b"}.merge({2: "c", 3: "d"}))

print(list({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}.filter(lambda x: x>2)))
print({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}.any(lambda x: x>2))
print({1, 2, 3}.sum())

print("http://httpbin.org/user-agent".request.get().json()["user-agent"])
