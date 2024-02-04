from pathlib import Path
def get_cats_info (path):
    cat_list=[]
    with open (path, 'r') as file:
        for line in file:
            data= line.strip().split (',')
            if len(data)== 3:
                try:
                    cat_info = {
                        "id": data[0],
                        "name": data[1],
                        "age": int(data[2])
                    }
                    cat_list.append(cat_info)
                except Exception as e:
                    traceback.print_exe()
            else:
                print(f"Ignoring invalid data: {line.strip()}")
                
    return cat_list

cats_info= get_cats_info ('cats.txt')
for cat in cats_info:
   print(cat)
