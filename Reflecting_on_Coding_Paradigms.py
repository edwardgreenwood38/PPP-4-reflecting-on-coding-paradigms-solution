
# function recursively flattens the nested list.
def flatten(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return [lst[0]] + flatten(lst[1:])

# function performs merge sort on a list
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

# function merges two sorted lists
def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

# function composes the two functions to first flatten the input list and then sorts it using merge sort
def flatten_and_sort(arr):
    return merge_sort(flatten(arr))

# Test
arr = [[3, 2, 1], [7, 9, 8], [6, 5, 4]]
print(flatten_and_sort(arr))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# How does this solution ensure data immutability?  the array 'arr' is not changed
# Is this solution a pure function? Why or why not? yes. it used multiple functions to flatten and sort the array
# Is this solution a higher order function? Why or why not? yes. it used multiple functions to flatten and sort the array
# Would it have been easier to solve this problem using a different programming style? no idea
# Why in particular is functional programming a helpful paradigm when solving this problem? it leaves the variable the same so that other areas of the code can use it as is

print("==================================================================")




# Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Example usage:
if __name__ == "__main__":
    # Creating instances of Podracer, AnakinsPod, and SebulbasPod
    podracer1 = Podracer(max_speed=500, condition="perfect", price=1000)
    anakins_pod = AnakinsPod(max_speed=600, condition="perfect", price=1500)
    sebulbas_pod = SebulbasPod(max_speed=550, condition="perfect", price=1200)

    print("Before repair:")
    print("Podracer1 condition:", podracer1.condition)
    podracer1.repair()
    print("After repair:")
    print("Podracer1 condition:", podracer1.condition)

    print("Before boost:")
    print("Anakin's Pod max speed:", anakins_pod.max_speed)
    anakins_pod.boost()
    print("After boost:")
    print("Anakin's Pod max speed:", anakins_pod.max_speed)

    print("Before flame jet:")
    print("Sebulba's Pod condition:", sebulbas_pod.condition)
    sebulbas_pod.flame_jet(podracer1)
    print("After flame jet:")
    print("Sebulba's Pod condition:", sebulbas_pod.condition)
    print("Podracer1 condition:", podracer1.condition)


# encapsulates the attributes (max_speed, condition, price) and methods (repair(), boost(), flame_jet()) within their respective classes
    
# abstraction the methods are hidden and the user does not need to know how they funciton to use them

# inheritance the other classes inherits from the Podracer class

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? no. as OOP grants flexability and reusability
    
# How in particular did Object Oriented Programming assist in the solving of this problem? by encapsulating the attributes and methods within their respective classes it made it easiser for reuseability

print("==================================================================")