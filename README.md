# codeDSA

Pattern	Time Complexity
Single loop	O(n)
Nested loops	O(n²), O(n³)...
Divide & conquer	O(log n), O(n log n)
Recursion	Depends: often O(2ⁿ)
Hash Table operations	O(1) avg, O(n) worst
Sorting (Timsort)	O(n log n)


Notation	Name	Example Algorithm
O(1)	Constant time	Accessing element by index
O(log n)	Logarithmic time	Binary Search
O(n)	Linear time	Loop through list
O(n log n)	Linearithmic time	Merge Sort, Quick Sort (avg case)
O(n²)	Quadratic time	Bubble Sort, nested loops
O(2ⁿ)	Exponential time	Recursive Fibonacci
O(n!)	Factorial time	Solving TSP with brute force



Type	Ordered	Mutable	Duplicate Allowed	Indexing	Key-Value


List	Yes	Yes	Yes	Yes	No
Tuple	Yes	No	Yes	Yes	No
Set	No	Yes	No	No	No
Dictionary	Yes	Yes	Keys → No, Values → Yes	Keys only	Yes

arr = arr[::-1]
arr[start:stop:step]
start: where to start (default is 0)

stop: where to end (default is end of list)

step: the step size (how much to move in each step)


 4. *args and **kwargs (Interview Favorite)
python
Copy
Edit
def total(*numbers):  # args = tuple
    return sum(numbers)

print(total(1, 2, 3, 4))  # 10
python
Copy
Edit
def display(**data):  # kwargs = dict
    for key, value in data.items():
        print(f"{key}: {value}")

display(name="Afreen", age=25)

nums = [1, 2, 3]
. Lambda Functions
Small one-line functions (anonymous)

python
Copy
Edit
add = lambda x, y: x + y
print(add(3, 4))  # 7
# map
squares = list(map(lambda x: x**2, nums))  # [1, 4, 9]

# filter
even = list(filter(lambda x: x % 2 == 0, nums))  # [2]



range(2, 4)
✅ Includes: 2 and 3
❌ Excludes: 4

  left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1