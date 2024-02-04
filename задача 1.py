from pathlib import Path

def total_salary (path):
    try:
         with open (path, 'r', encoding='UTF-8') as file:
              total_sum = 0
              total_count=0

              for line in file:
                data =line.strip().split (',')
                if len (data) ==2:
                     try:
                         salary = int(data[1]) 
                         total_sum +=salary
                         total_count +=1
                     except ValueError: 
                        print (f"Error parsing salary for {data[0]}: {data [1]} is not a valid number")
              if  total_count==0:
                    return 0, 0
                
              average=total_sum/total_count
              return total_sum, average     
    except FileNotFoundError:
        print (f"Error:  File {path} not found")
        return None
   
result=total_salary(Path(__file__ ). parent/'salary.txt')


if result is not None:
    total_sum, average=result
    print (f"Total Salary: {total_sum}, average: {int(average)}")   



             
