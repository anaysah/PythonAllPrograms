import time
start = time.time()
n = 56890
for r in range(100, 1000000):
	print(r)
	if r == n:
    print("ajay")
    break

end = time.time()
print(end-start)
