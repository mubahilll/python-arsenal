#rather than terminating function by return statement, we can pause the execution of func by storing th
#generators provide a simple way to create iterators

def demo():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


test = demo()
print(test)
print(next(test))
print(next(test))
print(next(test))

print("-"*10)
test2 = demo()

for a in test2:
    print(a)


def xor_static_key(a):
    key = 0x5
    for i in a:
        yield chr(ord(i) ^ key) 


for i in xor_static_key("test"):
    print(i)


xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "test") #anonymous generator expression
# print(xor_static_key2)
print("*"*10)
for i in xor_static_key2:
    print(i)
