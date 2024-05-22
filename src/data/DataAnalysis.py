import random
import json

with open('./DataApi.json') as f:
    appi_data = json.load(f)

##-----------------------------------------------------------General Data
initialAsist = 180100

#Lista bandas
List_Band_21 = appi_data[0]['Bands'] 
List_Band_22 = appi_data[1]['Bands']
List_Band_23 = appi_data[2]['Bands']

#rangos de crecimiento estimado
GrowthLevel1 = [28,35]
GrowthLevel2 = [20,28]
GrowthLevel3 = [15,25]
GrowthLevel4 = [8,13]

##------------------------------------Graph 1: Artistas: año, nombre, share, total income
List_topBand_21 = []
List_shareBand_21 = []
List_Collected_21 = appi_data[0]['Income']

List_topBand_22 = []
List_shareBand_22 = []
List_Collected_22 = appi_data[1]['Income']

List_topBand_23 = []
List_shareBand_23 =  []
List_Collected_23 = appi_data[2]['Income']

##------------------------------------Graph 2: Growth: #año, asistentes, precio ticket, ingreso total, porcentaje de crecimiento
asistentes_21 = appi_data[0]['Asistants']
porcentajeAlcance_21 = ((asistentes_21 - initialAsist)*100)/asistentes_21
ingresoTotal_21 = List_Collected_21
price_21 = appi_data[0]['Ticketprice']

asistentes_22 = appi_data[1]['Asistants']
porcentajeAlcance_22 = ((asistentes_22 - asistentes_21)*100)/asistentes_22
ingresoTotal_22 = List_Collected_22
price_22 = appi_data[1]['Ticketprice']

asistentes_23 = appi_data[2]['Asistants']
porcentajeAlcance_23 = ((asistentes_23 - asistentes_22)*100)/asistentes_23
ingresoTotal_23 = List_Collected_22
price_23 = appi_data[2]['Ticketprice']

##------------------------------------Graph 3 DATA: #nombre, nivel, nivel nuevo, seguidores actuales, seguidores nuevos, porcentaje crecimiento, url, imag
List_bandLevel_21 = []
List_bandLevel_New21 = []
List_bandFollow_21 = []
List_bandFollow_New21 = []
List_growth_21 = []
urlBand_21 = []
imgBand_21 = []


List_bandLevel_22 = []
List_bandLevel_New22 = []
List_bandFollow_22 = []
List_bandFollow_New22 = []
List_growth_22 = []
urlBand_22 = []
imgBand_22 = []


List_bandLevel_23 = []
List_bandLevel_New23 = []
List_bandFollow_23 = []
List_bandFollow_New23 = []
List_growth_23 = []
urlBand_23 = []
imgBand_23 = []
##------------------------------------Graph 4 Level: #por nivel por año
levels_2021 = [0,0,0,0]
levels_2022 = [0,0,0,0]
levels_2023 = [0,0,0,0]

##-----------------------------------------------------------Funciones analisis
def getGrowth(level): 
    if (level == 1):
        return (random.randrange(GrowthLevel1[0], GrowthLevel1[1]))*0.01
    elif (level == 2):
        return (random.randrange(GrowthLevel2[0], GrowthLevel2[1]))*0.01
    elif (level == 3):
        return (random.randrange(GrowthLevel3[0], GrowthLevel3[1]))*0.01
    elif (level == 4):
        return (random.randrange(GrowthLevel4[0], GrowthLevel4[1]))*0.01
    
def checkNewFollow(Followers, growth):
    newF = Followers+int(Followers*growth)
    return newF

def checkNewLevel(Followers):
    if(Followers > 10000000):
        return 1
    elif(Followers < 10000000 and Followers >= 1000000):
        return 2
    elif(Followers < 1000000 and Followers >= 100000):
        return 3
    elif(Followers < 100000):
        return 4

def computeShare(Top10Follow, totalFollow, generalIncome, List_shareBand):
    lastShare = generalIncome

    for i in range(0,9):
        porcent = int((Top10Follow[i]*100)/totalFollow)
        share = generalIncome*(porcent*0.01)
        List_shareBand.append(share)
    for j in List_shareBand:
        lastShare -= j
    List_shareBand.append(lastShare)

##-----------------------------------------------------------Analyse graph
def graph1():#########################
    totalFollow_21 = 0
    Top10Follow_21 = []
    OtherFollow_21 = 0
    generalIncome_21 = List_Collected_21

    totalFollow_22 = 0
    Top10Follow_22 = []
    OtherFollow_22 = 0
    generalIncome_22 = List_Collected_22

    
    totalFollow_23 = 0
    Top10Follow_23 = []
    OtherFollow_23 = 0
    generalIncome_23 = List_Collected_23

    parcialFollowers=[]
    parcialFollowersName=[]

    ##---------------------------Compute 2021
    for band in List_Band_21:
        totalFollow_21 += band['Followers']
        parcialFollowers.append(band['Followers'])
        parcialFollowersName.append(band['Name'])
    #print(parcialFollowers)
    parcialFollowers2 = sorted(parcialFollowers, reverse=True)
    #print(parcialFollowers)
    cont=1
    for follow in parcialFollowers2:
        if (cont < 10):
            Top10Follow_21.append(follow)
            cont+=1
        else:
            OtherFollow_21 += follow
    Top10Follow_21.append(OtherFollow_21)
    #print(Top10Follow_21)

    computeShare(Top10Follow_21, totalFollow_21, generalIncome_21, List_shareBand_21)

    index=0
    for i in Top10Follow_21:
        for j in parcialFollowers:
            if (i == j):
                List_topBand_21.append(parcialFollowersName[index])
                break
            index = index+1
        index=0
    List_topBand_21.append("Other")
    #print(List_topBand_21) 

    ##---------------------------Compute 2022
    parcialFollowers.clear()
    parcialFollowersName.clear()

    for band in List_Band_22:
        totalFollow_22 += band['Followers']
        parcialFollowers.append(band['Followers'])
        parcialFollowersName.append(band['Name'])
    #print(parcialFollowers)
    parcialFollowers2 = sorted(parcialFollowers, reverse=True)
    #print(parcialFollowers)
    cont=1
    for follow in parcialFollowers2:
        if (cont < 10):
            Top10Follow_22.append(follow)
            cont+=1
        else:
            OtherFollow_22 += follow
    Top10Follow_22.append(OtherFollow_22)
    #print(Top10Follow_22)

    computeShare(Top10Follow_22, totalFollow_22, generalIncome_22, List_shareBand_22)

    index=0
    for i in Top10Follow_22:
        for j in parcialFollowers:
            if (i == j):
                List_topBand_22.append(parcialFollowersName[index])
                break
            index = index+1
        index=0
    List_topBand_22.append("Other")
    #print(List_topBand_22) 

    ##---------------------------Compute 2023
    parcialFollowers.clear()
    parcialFollowersName.clear()

    for band in List_Band_23:
        totalFollow_23 += band['Followers']
        parcialFollowers.append(band['Followers'])
        parcialFollowersName.append(band['Name'])
    #print(parcialFollowers)
    parcialFollowers2 = sorted(parcialFollowers, reverse=True)
    #print(parcialFollowers)
    cont=1
    for follow in parcialFollowers2:
        if (cont < 10):
            Top10Follow_23.append(follow)
            cont+=1
        else:
            OtherFollow_23 += follow
    Top10Follow_23.append(OtherFollow_23)
    #print(Top10Follow_23)

    computeShare(Top10Follow_23, totalFollow_23, generalIncome_23, List_shareBand_23)

    index=0
    for i in Top10Follow_23:
        for j in parcialFollowers:
            if (i == j):
                List_topBand_23.append(parcialFollowersName[index])
                break
            index = index+1
        index=0
    List_topBand_23.append("Other")
    #print(List_topBand_23) 


def graph3():
    for band in List_Band_21:
        growthBand = getGrowth(band['Level'])
        List_growth_21.append(growthBand)

        List_bandFollow_21.append(band['Followers'])
        NewFollow = checkNewFollow(band['Followers'], growthBand)
        List_bandFollow_New21.append(NewFollow)

        List_bandLevel_21.append(band['Level'])
        NewLevel = checkNewLevel(NewFollow)
        List_bandLevel_New21.append(NewLevel)
        urlBand_21.append(band['Url'])
        imgBand_21.append(band['Image'])
        
    for band in List_Band_22:
        growthBand = getGrowth(band['Level'])
        List_growth_22.append(growthBand)

        List_bandFollow_22.append(band['Followers'])
        NewFollow = checkNewFollow(band['Followers'], growthBand)
        List_bandFollow_New22.append(NewFollow)

        List_bandLevel_22.append(band['Level'])
        NewLevel = checkNewLevel(NewFollow)
        List_bandLevel_New22.append(NewLevel)
        urlBand_22.append(band['Url'])
        imgBand_22.append(band['Image'])

        
    for band in List_Band_23:
        growthBand = getGrowth(band['Level'])
        List_growth_23.append(growthBand)

        List_bandFollow_23.append(band['Followers'])
        NewFollow = checkNewFollow(band['Followers'], growthBand)
        List_bandFollow_New23.append(NewFollow)

        List_bandLevel_23.append(band['Level'])
        NewLevel = checkNewLevel(NewFollow)
        List_bandLevel_New23.append(NewLevel)
        urlBand_23.append(band['Url'])
        imgBand_23.append(band['Image'])

def graph4():
    for band in List_Band_21:
        if(band['Level'] == 1):
            levels_2021[0] += 1
        elif(band['Level'] == 2):
            levels_2021[1] += 1
        elif(band['Level'] == 3):
            levels_2021[2] += 1
        elif(band['Level'] == 4):
            levels_2021[3] += 1
    
    for band in List_Band_22:
        if(band['Level'] == 1):
            levels_2022[0] += 1
        elif(band['Level'] == 2):
            levels_2022[1] += 1
        elif(band['Level'] == 3):
            levels_2022[2] += 1
        elif(band['Level'] == 4):
            levels_2022[3] += 1
    
    for band in List_Band_23:
        if(band['Level'] == 1):
            levels_2023[0] += 1
        elif(band['Level'] == 2):
            levels_2023[1] += 1
        elif(band['Level'] == 3):
            levels_2023[2] += 1
        elif(band['Level'] == 4):
            levels_2023[3] += 1

##-----------------------------------------------------------Set New Data
graph1()
graph3()
graph4()


##-------------------------------------------------------------------------------JSON
for i in range(0,len(List_Band_21)):
    List_Band_21[i]['Growth']= List_growth_21[i]
    List_Band_21[i]['nivelNew']= List_bandLevel_New21[i]
    List_Band_21[i]['followNew']= List_bandFollow_New21[i]

for i in range(0,len(List_Band_22)):    
    List_Band_22[i]['Growth']= List_growth_22[i]
    List_Band_22[i]['nivelNew']= List_bandLevel_New22[i]
    List_Band_22[i]['followNew']= List_bandFollow_New22[i]

for i in range(0,len(List_Band_23)):
    List_Band_23[i]['Growth']= List_growth_23[i]
    List_Band_23[i]['nivelNew']= List_bandLevel_New23[i]
    List_Band_23[i]['followNew']= List_bandFollow_New23[i]

##-------------------------------------------------------------------------------JSON
x = {
    "GraphArtistas":{
        "2021": {
            "Band": List_topBand_21,
            "Share": List_shareBand_21,
            "Collected": List_Collected_21,
        },
        "2022": {
            "Band": List_topBand_22,
            "Share": List_shareBand_22,
            "Collected": List_Collected_22,
        },
        "2023": {
            "Band": List_topBand_23,
            "Share": List_shareBand_23,
            "Collected": List_Collected_23,
        },
    },
    "GraphGrowth":{ 
        "2021": {
            "asistentes" : asistentes_21,
            "porcentajeGrowth" : porcentajeAlcance_21,
            "ingreso" : ingresoTotal_21,
            "tiketPrice" : price_21,
        },
        "2022": {
            "asistentes" : asistentes_22,
            "porcentajeGrowth" : porcentajeAlcance_22,
            "ingreso" : ingresoTotal_22,
            "tiketPrice" : price_22,
        },
        "2023": {
            "asistentes" : asistentes_23,
            "porcentajeGrowth" : porcentajeAlcance_23,
            "ingreso" : ingresoTotal_23,
            "tiketPrice" : price_23,
        },
    },
    "GraphData":{
        "2021":{
            "bands": List_Band_21,
        },
        "2022":{
            "bands": List_Band_22,
        },
        "2023":{
            "bands": List_Band_23,
        },
    },
    "GraphLevel":{
        "2021": levels_2021,
        "2022": levels_2022,
        "2023": levels_2023,
    },
}
#print(x)
 
y = json.dumps(x)
    
with open('./DataOutput.json', 'w') as f:
    f.write(y)