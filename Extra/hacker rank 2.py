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

### Nested list ###
if __name__ == '__main__':
    studs=[] #created empty list 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studs.append([name,score])
        #now empty list wil be filled

    #for all unique grades i use list comprehension
    grades = sorted(list(set([score for name,score in studs])))
    second_lowest = grades[1]   #2nd lowest grade

    runner_up_students = [name for name, score in studs if score == second_lowest]   

    runner_up_students.sort() #to sort names in alphabetically
    for name in runner_up_students:
      print(name) 
