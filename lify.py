from queue import Queue as que
import random

#defenitions:

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

def seperation():
        for x in iq:
                if x>=4 and x<=7:
                        q47.append(x)
                elif x>=8 and x<=11:
                        q811.append(x)
                elif x>=12 and x<=15:
                        q1215.append(x)
                        
def max_floor(lst):
        dictionary=find_frequencies(lst)
    # Base case: dictionary with only one element
        if len(dictionary) == 1:
                return max(dictionary, key=dictionary.get)
    
    # Divide the dictionary into two halves
        mid = len(dictionary) // 2
        left_dict = {k: v for i, (k, v) in enumerate(dictionary.items()) if i < mid}
        right_dict = {k: v for i, (k, v) in enumerate(dictionary.items()) if i >= mid}
    
    # Recursively find maximum key-value pairs in left and right halves
        max_left = max_floor(left_dict)
        max_right = max_floor(right_dict)
    
    # Compare and return the key with the highest value
        if dictionary[max_left] > dictionary[max_right]:
                return max_left
        else:
                return max_right



def find_frequencies(lst):
        frequencies = {}
        for item in lst:
                if item in frequencies:
                        frequencies[item] += 1
                else:
                        frequencies[item] = 1
        return frequencies

        
#initial queue
iq = []
#queue for each lift
q47 = []
q811=[]
q1215=[]


#initial queue generator and printing
print("Initial Queue of people")
for x in range(0,50):
    iq.append(random.randint(4,15))
    print(iq[x])

#sorting queue
size = len(iq)
quickSort(iq, 0, size-1)

#printing sorted queue
print("\n\nSorted Queue of people")
for x in range(0,50):
        print(iq[x])

#seperating queues and printing
seperation()
print("\n\nSeperated Queue: ")
print("4 to 7\t\t\t8 to 11\t\t\t12 to 15\n")

max_length = max(len(q47), len(q811), len(q1215))
for x in range(max_length):
    output_line = ""
    if x < len(q47) and q47[x] is not None:
        output_line += str(q47[x]) + '\t\t\t'
    else:
        output_line += ' - ' +'\t\t\t'
    if x < len(q811) and q811[x] is not None:
        output_line += str(q811[x]) + '\t\t\t'
    else:
        output_line += ' - ' +'\t\t\t'
    if x < len(q1215) and q1215[x] is not None:
        output_line += str(q1215[x]) + '\t\t\t'
    else:
        output_line += ' - ' +'\t\t\t'
    print(output_line)

f47=max_floor(q47)
print("Lift 1 goes to : "+str(f47))

f811=max_floor(q811)
print("Lift 2 goes to : "+str(f811))

f1215=max_floor(q1215)
print("Lift 3 goes to : "+str(f1215))
