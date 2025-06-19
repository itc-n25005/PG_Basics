import csv

movies = [["トップガン","リスキービジネス","マイノリティーレポート"],["タイタニック","レヴェナント","インセプション"],["トレーニング・デイ","マン・オン・ワイヤー","フライト"]]

with open("ch1.csv","w") as f:
    r = csv.writer(f,delimiter=",")
    for row in movies:
        r.writerow(row)




