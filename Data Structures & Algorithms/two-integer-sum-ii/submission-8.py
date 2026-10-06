class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maxx = max(numbers)
        no = -float('inf')
        for i in range(len(numbers)):
            if numbers[i]==no:
                continue

            value = target - numbers[i]
            
            if value>maxx:
                no = numbers[i]
                continue

            
            j = i+1
            while j<len(numbers):
                if numbers[j]<value:
                    j+=1
                elif numbers[j]==value:
                    return [i+1,j+1]
                else:
                    break


