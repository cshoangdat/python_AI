file = open("test.txt", "r")
line = file.readline()
a = int(line[0]);
b = int(line[2]);
file_out = open("TONG.txt","w"); 
file_out.write(str(a+b))
file_out.close()
file.close()