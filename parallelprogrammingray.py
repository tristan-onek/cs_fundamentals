import ray # using Ray given Python's design
ray.init()

@ray.remote
def solve1(a):
    return 1

@ray.remote
def solve2(b):
    return 2
  
x1 = solve1.remote(0)
y1 = solve2.remote(1)
x, y = ray.get([x1, y1])
