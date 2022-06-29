data =input()   
su=0
sis=0
dia=0
n=0         # sucursal
k=0         # medicamento
m=0         # paciente
InI =[]
InP =[]
InF =[] 
InM=0
Inm=0
SuM=0
Sum=0    
data = data.split()
n=int(data[0])
for x in range(n):
    datos=input()
    InI.append(datos)
    InP.append(0)
    InF.append(0)
k=int(data[1])
for x in range(k):
    k = k  
m=int(data[2])
for x in range(m):
    datos=input()
    data=datos.split() 
    n=int(data[0])
    k=int(data[1])
    InI=int(data[2])
    sis=int(data[3])
    dia=int(data[4])        
# for x in range(n):
#     InF[x]=int(InI[x])-int(InP[x])
# InM=InF[0]
# Inm=InF[0]    
for x in range(n):
    if InF[x]>InM:
        InM=InF[x]
        SuM=x   
    if InF[x]<Inm:
        Inm=InF[x] 
        Sum=x
print(su)
print(n)
print(k)
print(sis)
print(dia)
print(m)
print(InP)
print(InF)
print(InM)
print(Inm)
print(Sum)
print(Sum)

# print(Sum +1, Inm)
# print(SuM +1, InM)
# for x in range(n):
#     print(x+1, "{:.2f}%".format((float(InP[x])/float(InI[x]))*100))





