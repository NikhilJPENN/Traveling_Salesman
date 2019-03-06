import math
import random
def read_cities(file_name) :
    city_list=[]
    road_map=[]
    for line in (file_name):
        city_list.append(list(line.strip('\n').split('\t')))

    city_list.append(city_list[0])   ## First element added at the last position to make it cycle

    for row in city_list:
        row[2] = float(row[2])
        row[3] = float(row[3])

    for l in city_list:
        road_map.append(tuple(l))

    return (road_map)
    
def print_cities(road_map):
    
    print("list of cities along with their location")
    for i in range(len(road_map)):
       print(road_map[i][0],"\t", road_map[i][1],"\t","%0.2f" %road_map[i][2],"\t","%0.2f" %road_map[i][3])
       
       print("")    
       
def compute_total_distance(road_map):
    x=[]
    y=[]
    distance=[]
    total_distance=0
    for i in range((len(road_map))-1):
        
        x.append(((road_map[i][2])-(road_map[i+1][2])))
        y.append((road_map[i][3])-(road_map[i+1][3]))
        
        distance.append(math.sqrt(math.pow(x[i],2)+math.pow(y[i],2)))
       
    total_distance=sum(distance)
    
    return (total_distance)

def swap_cities(road_map, index1, index2):
    
    if (index1==index2):
        #for i in range(len(road_map)-1)
        #    x[i]=(road_map[i][2])-(road_map[i+1][2])
        #    y[i]=(road_map[i][3])-(road_map[i+1][3])
        #    distance[i]=math.sqrt(math.pow(x[i],2)+math.pow(y[i],2))
        #total_distance=sum(distance)

        total_distance=compute_total_distance(road_map)    
        new_data=(road_map,total_distance)
        
        return (new_data)

    else:
        #print (road_map)
        new_road_map=road_map 
        temp=new_road_map[index1]
        new_road_map[index1]=new_road_map[index2]
        new_road_map[index2]=temp
        
        l=len(new_road_map)
    
        new_road_map[l-1]=new_road_map[0]
        
        #for i in range(len(new_road_map)-1):
        #    x[i]=(new_road_map[i][2])-(new_road_map[i+1][2])
        #    y[i]=(new_road_map[i][3])-(new_road_map[i+1][3])
        #    new_distance[i]=math.sqrt(math.pow(x[i],2)+math.pow(y[i],2))

        #new_total_distance=sum(new_distance)
        total_distance=compute_total_distance(new_road_map)
    
        new_data=(new_road_map, total_distance) 
        return (new_data)

def find_best_cycle(road_map):
    
    new_data=[]
    
    for i in range(50):
        index=random.sample(range(50), 2)
        index1=index[0]
        index2=index[1]
        swap_data=swap_cities(road_map,index1,index2)
        new_data.append(swap_data)
        
        #(swap_road_map,swap_distance)=sorted(new_data,key=lambda x: x[1], reverse=False)[0]
    (swap_road_map,swap_distance)=min(new_data,key=lambda item:item[1])
    #min_d_data.append(swap_road_map,swap_distance)
    
    #(best_road_map,best_distance)=sorted(min_d_data,key=lambda x: x[1], reverse=False)[0]
    #(best_road_map,best_distance)=min(min_d_data,key=lambda item:item[1])
    #return ((best_road_map,best_distance))
    return(swap_road_map,swap_distance)


def print_map(road_map):
    #print ('State', 'City', "latitude", "longitude")
    x=[]
    y=[]
    distance=[]
    
    for i in range((len(road_map))-1):
        
        x.append(((road_map[i][2])-(road_map[i+1][2])))
        y.append((road_map[i][3])-(road_map[i+1][3]))
        
        distance.append(math.sqrt(math.pow(x[i],2)+math.pow(y[i],2)))
       
    print("list of cities along with their location and corresponding distances")
    for i in range(len(road_map)):
       
        print(road_map[i][0], road_map[i][1],"", "%0.2f" %road_map[i][2],"", "%0.2f" %road_map[i][3],"","%0.2f" %distance[i-1])
        print("")

    
            
def main():
    city_data=open('C:\\Users\\jamdadenikhil\\Desktop\\CIT 590\Homework 4\\city-data.txt','r')  #r+ : both read and write
    road_map=read_cities(city_data)
    print_cities(road_map)
    x=0
    best_map=[]
    
    while(x<=2):
                
        random.shuffle(road_map)
        a=len(road_map)
        road_map[a-1]=road_map[0]
        best_cycle=find_best_cycle(road_map)
        
        best_map.append(best_cycle)
        x=x+1
       
    
    
    print("Three best Road Map distances:")
    print ("%0.2f" %best_map[0][1])
    print ("%0.2f" %best_map[1][1])
    print ("%0.2f" %best_map[2][1])
    print ("")    
    print ("Least distance Raod Map")
   
    (final_road_map,min_dist)=min(best_map,key=lambda item:item[1])
    print ("")
    print("%0.2f" %min_dist)
    print ("\n")
    print_map(final_road_map)
    city_data.close()


main()
        
    

    


