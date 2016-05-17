import csv

if __name__ == "__main__":

    f = open('newfile.csv', 'w')
    writer2=csv.writer(f)
    str=[]

    with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for rows in reader:
            str=[]
            for row in rows:
                if row =='critical':
                    row=row.replace('critical','HIGH')
                elif row =='high':
                    row=row.replace('high','MEDIUM')
                elif row =='medium':
                    row=row.replace('medium','LOW')

                str.append(row)
            writer2.writerow(str)



