import imba

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

imba.install("requests")
print("http://httpbin.org/user-agent".request.get().json()["user-agent"])

imba.install("json")
print("{\"a\": [1, \"test\", 3.14]}".json)
print([1, {1: "a"}].asjson)

print(range(10).map(str).reduce(imba.op.add))

print([[1, 2, 3], [4, 5, 6]].join(0))

print(
    range(1,11)
        .map(lambda row: range(1,11)
        .map(lambda col: row*col))
        .map(lambda row: row.fmt("{:4}")).join("\n")
)
