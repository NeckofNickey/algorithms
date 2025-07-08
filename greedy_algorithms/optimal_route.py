# https://informatics.msk.ru/mod/statements/view.php?id=77798&chapterid=113075#1

def get_optimal_route(n, k, gas_station_list):
    
    current_stop = 0 #текущая остановка
    last_stop = 0 #последняя остановка
    stops = 0
    gas_station_index = 0
    
    while current_stop + k < n:
        
        while gas_station_index < len(gas_station_list) and gas_station_list[gas_station_index] <= current_stop + k:
            last_stop = gas_station_list[gas_station_index]
            gas_station_index += 1
        
        if last_stop == current_stop:
            return -1
        
        current_stop = last_stop
        stops += 1
    
    return stops
        
    
            
            
n, k = list(map(int, input().split()))

gas_station_list = list(map(int, input().split()))[1:]

print(get_optimal_route(n, k, gas_station_list))

