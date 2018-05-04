ranks=[0]*1000
import csv
def preprocess(file_path):
	file=open(file_path)
	read=csv.reader(file)
	data=list(read)
	for i in range(1000):
		data[i][1]=float(data[i][1])
		data[i][0]=int(data[i][0])
	data.sort(key=lambda s:s[1],reverse=True)
	r=1
	
	mark_prev=data[0][1]
	for i in range(1000):
		if(data[i][1]!=mark_prev):
			ranks[r]=(i-r+1)
			r=i+1
			mark_prev=data[i][1]
		
		data[i].append(r)
	
	return data

def main(data):
	while(True):
		buff=input("Enter Roll No.")
		
		if(buff=="stop"):
			break
		roll=int(buff)
		b=[t for t in data if t[0]==roll][0]
		tied=ranks[b[2]]
		print("Marks : ",b[1],"Rank : ",b[2],"Tied : ",tied)

main(preprocess('G:\\Marksheet.csv'))


