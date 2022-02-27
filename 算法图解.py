# def binary_search(list,item):
#     low=0
#     high=len(list)-1
#
#     while low<=high:
#         mid=(low+high)
#         guess=list[mid]
#         if guess==item:
#             return mid
#         if guess>item:
#             high=mid-1
#         else:
#             low=mid+1
#     return None
#
# my_list=[1,3,5,7,9]
# print(binary_search(my_list,7))
#
# def find_smallest(arr): #找出最小的数
#     smallest=arr[0]
#     smallest_index=0
#     for i in range(1,len(arr)):
#         if arr[i]<smallest:
#             smallest=arr[i]
#             smallest_index=i
#             pass
#         pass
#     return smallest_index
#
# def selection_test(arr):
#     newArr=[]
#     for i in range(len(arr)):
#         smallest=find_smallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# print(selection_test([1,3,5,4,9]))

#贪婪算法
#
# status_needed={('mt','wa','or','id','nv','ut','ca','az')}#需要覆盖的州
# stations={}
# stations['kone']= {('id','nv','ut')} #可选择的电视台
# stations['kewo']={('wa','id','mt')}
# stations['kthree']={('or','nv','ca')}
# stations['kfour']={('nv','ut')}
# stations['kfive']={('ca','za')}
# final_stations=[]
#
# best_station=None #能覆盖最多未覆盖州的电视台
# states_coved=set()
# for stations,states_for_station in stations.items():
#     coverd=status_needed & states_for_station #该电视台能够覆盖的未覆盖的州
#     if len(coverd)>len(states_coved):
#         best_station=stations
#         states_coved=coverd
#
# final_stations.append(best_station)
# status_needed-=states_coved
# print(final_stations)





