# def solution(bridge_length, weight, truck_weights):
#     from collections import deque
#     answer = 0
#     truck_weights = deque(truck_weights)
#     on_bridge = []
#     bbb = []
#     seconds = [0]*len(truck_weights)
#     idx=0
#     while True:
#         if len(bbb) < bridge_length and sum([i[1] for i in bbb])+truck_weights[0] <=weight:
#                 a = truck_weights.popleft()
#                 on_bridge.append([idx, a, True])
#                 bbb.append([idx,a])
#                 idx +=1
#         if not len(truck_weights):
#             answer+= bridge_length+1
#             return answer
#         for i in on_bridge:
#             if i[2]==True:
#                 seconds[i[0]]+=1
#                 if seconds[i[0]]==bridge_length:
#                     i[2] =False
#                     bbb.remove([i[0],i[1]])
#         answer+=1

def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    return answer

print(solution(5,5,[2,2,2,2,1,1,1,1]))
# print(solution(100,100,[10]))
# print(solution(2,10, [7,4,5,6]))
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))