# Creating a class for array

class Array():
    def __init__(self, length):
        self.length = length
        self.arr = [0] * length
        self.count = 0
    
    def array_print(self):
        if self.count > 0:
            for i in range(self.count):
                if i == 0:
                    print(f"[{self.arr[i]}, ", end="")
                elif i == self.count - 1:
                    print(f"{self.arr[i]}]", end="")
                else:
                    print(f"{self.arr[i]}, ", end="")
                    

        else:
            print("Array is empty")

    def array_append(self, item):
        if self.count < self.length:
            self.arr[self.count] = item
        else:
            self.length *= 2
            new_array = [0] * self.length

            for i, element in enumerate(self.arr):
                new_array[i] = element
            
            self.arr = new_array
            self.arr[self.count] = item
        
        self.count += 1

    def array_index(self, item):
        index = -1
        for i, element in enumerate(self.arr):
            if item == element:
                index = i
        
        print(index)

    
array = Array(3)

array.array_append(20)
array.array_append(30)
array.array_append(40)
array.array_append(50)
array.array_append(60)
array.array_index(40)

array.array_print()