# O(n log(n))

class MergeSort:
    def merge(self, left, right):
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right): # stop when one of the lists is exhausted
            print(f'left[i]: {left[i]} right[j]: {right[j]}')
            if left[i] <= right[j]: 
                print(f'Appending {left[i]} to the result')
                merged.append(left[i])
                print(f'result now is {merged}')
                i += 1
                print(f'i now is {i}')
            else:
                print(f'Appending {right[j]} to the result')
                merged.append(right[j])
                print(f'result now is {merged}')
                j += 1
                print(f'j now is {j}')

        print('One of the lists is exhausted. Adding the rest of one of the lists.')
        merged += left[i:]
        merged += right[j:]
        print(f'result now is {merged}')

        return merged
    
    #sort smallest to biggest
    def mergeSort(self, nums):
        print('---')
        print(f'mergesort on {nums}')
        if len(nums) < 2:
            print('length is 1: returning the list without changing')
            print('---')
            return nums
        
        middle = int(len(nums) / 2)
        print(f'calling mergesort on {nums[:middle]}')
        left = self.mergeSort(nums[:middle])
        print(f'calling mergesort on {nums[middle:]}')
        right = self.mergeSort(nums[middle:])
        print(f'Merging left: {left} and right: {right}')
        print(f'exiting mergesort on {nums}')
        print('#---')
        return self.merge(left,right)


mergesort = MergeSort()


print(mergesort.mergeSort([4,1,6,2]))
