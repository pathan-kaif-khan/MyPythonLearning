### list comprehension ###
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
result = [[i, j, k] 
          for i in range (x + 1) 
          for j in range (y + 1) 
          for k in range (z + 1) 
          if (i+j+k) != n]
print(result)

### find the runner up ###
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uniqueScores = set(arr)
    #To get rid of duplicate values i typecast list to set
    uniqueScores.remove(max(uniqueScores))
    #here remove the max score which is the winner but we need runner up in this question so we remove winner
    print(max(uniqueScores))
    #after removing winner we left with the runner up 

### ###
