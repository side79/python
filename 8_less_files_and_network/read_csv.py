import csv
import os

def read_csv_cars():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'cars.csv')
    print("script_dir=", script_dir)
    print("file_path=", file_path)
    with open(file_path) as f:
        csv_reader = csv.reader(f, delimiter=',')
        lines_count = 0
        print('csv_reader', csv_reader)
        for row in csv_reader:
            #print(repr(row))
            if lines_count == 0:
                print("Columns:", " | ".join(row))
            else:
                #print("values", " , ".join(row))
                print(f"Car from {row[0]} by {row[1]} ({row[2]}) [{row[3]}], price={row[4]}")
            lines_count += 1

def read_csv_cars_to_dict():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'cars.csv')
    
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        print("csv_reader", csv_reader)
        lines_count = 0
        for row in csv_reader:
            #print(repr(row))
            if lines_count == 0:
                print("Columns", " | ".join(row))
            print(
                f"Car from {row['year']} "
                f"by {row['name']} "
                f"({row['vendor']}) "
                f"[{row['comment']}] "
                f"price={row['price']}"
            )
            lines_count += 1
            
def write_csv_dict():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employee_bithday_months.csv')
    FILD_NAME = "name"
    FILD_DEPARTMENT = "depadtment"
    FILD_DM = "birth month"
    with open(file_path, "w") as f:
        fildnames = [
            FILD_NAME,
            FILD_DEPARTMENT,
            FILD_DM
        ]
        csv_writer = csv.DictWriter(f, fieldnames=fildnames, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        csv_writer.writeheader()
        csv_writer.writerow({
            FILD_NAME: "John Smith",
            FILD_DEPARTMENT: "IT",
            FILD_DM: "March"
        })
        
        csv_writer.writerow({
            FILD_NAME: "Ann White",
            FILD_DEPARTMENT: "HH",
            FILD_DM: "Sept"
        })
        
        csv_writer.writerow({
            FILD_NAME: "Ann Bleck",
            FILD_DEPARTMENT: "HH, manager, coche",
            FILD_DM: ""
        })

if __name__ == '__main__':
    #read_csv_cars()
    #read_csv_cars_to_dict() 
    
    write_csv_dict()       
