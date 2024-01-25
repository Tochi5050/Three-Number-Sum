#Time Complexity - O(n^2)
#Space Complexity - O(n)

def threeNumberSum(array, targetSum):
  return subThreeNumSum(array, 0, targetSum, [])


def subThreeNumSum(array, targetPointerIdx, targetSum, targetSumArr):
  array.sort()
  targetPointerIdx += 0 
  leftPointerIdx = targetPointerIdx + 1
  rightPointerIdx = len(array) - 1
  targetSumNewArr = targetSumArr
  
  while leftPointerIdx < rightPointerIdx:
      
      
      while leftPointerIdx < rightPointerIdx:
        
        arrTargetSum = array[targetPointerIdx] + array[leftPointerIdx] + array[rightPointerIdx]
        
        if arrTargetSum == targetSum:
          targetSumNewArr.append([array[targetPointerIdx], array[leftPointerIdx], array[rightPointerIdx]])
          leftPointerIdx += 1
          rightPointerIdx -= 1
        elif arrTargetSum < targetSum:
          leftPointerIdx += 1
        elif arrTargetSum > targetSum:
          rightPointerIdx -= 1
      
 
  
  
      subThreeNumSum(array, targetPointerIdx + 1, targetSum, targetSumNewArr)
  return targetSumNewArr
    
  





#Test case 1

newArr = [12, 3, 1, 2, -6, 5, -8, 6]
sum = 0
print(threeNumberSum(newArr, sum))