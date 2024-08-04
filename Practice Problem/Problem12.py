def generateTable(n):
    table =""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"Practice Problem/Tables/table_{n}.txt" , "w") as f:
        f.write(table)
    
for i in range(2,10):
    generateTable(i)