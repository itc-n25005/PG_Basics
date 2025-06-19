import csv

movies = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("ch.csv","w") as f:
    r = csv.writer(f,delimiter=",")
    for row in movies:
        r.writerow(row)




