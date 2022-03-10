
# this implementation bubbles the smallest numbers to the front of the list
def bubble_sort(arr):
    # 'bubble' the smallest element to the front
    for i in range(len(arr)):
        elem_check = arr[i]
        smallest_elem_index = i
        # change the starting point for each sorting cycle
        for j in range(i,len(arr)):
            # sorting cycle
            secondary_elem_check = arr[j]
            is_this_a_smaller_element = True if secondary_elem_check < elem_check else False
            # if a smaller element is detected
            if is_this_a_smaller_element:
                elem_check = secondary_elem_check
                smallest_elem_index = j
        # swap the first element with the smallest element a.k.a "bubble" the smallest element
        arr[i],arr[smallest_elem_index] = arr[smallest_elem_index],arr[i]
    return arr




def insertion_sort(arr):
    # start from 1 because the first element is assumed to be part of the
    # sorted array
    for i in range(1,len(arr)):
        position = i
        new_element_to_add = arr[i]
        # position has to be greater than 0 and 0 is the last element in the sorted arr
        # the while loop keeps running until the larger element is inserted in the proper position in
        # the sorted arr
        while position > 0 and arr[position-1] > new_element_to_add:
            # swap the larger element with the smaller element
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = new_element_to_add
    return arr
#print(insertion_sort([5,4,2,8,9,0,1]))





def partition(left,right,arr):
    pivot_index = left
    pivot_value = arr[left]
    while left < right:
        # keep moving right from left, find the element that is greater than the pivot
        while left < len(arr) and arr[left] <= pivot_value:
            left += 1
        # keep moving left from right, find the element that is lower than the pivot
        while arr[right] > pivot_value:
            right -= 1
        # when both pointers are pointing at the correct elements, swap the elements
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
    # the while loop above exits when the left index > right index
    # now we swap the left index (pointing to value higher than the pivot) and the pivot
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    # arr[right] is the new pivot
    return right

def quick_sort(left,right,arr):
    if left < right:
        pivot_index = partition(left,right,arr)
        # quick sort the left side (all values lesser than pivot)
        quick_sort(left,pivot_index-1,arr)
        # quick sort the right side (all values greater than pivot)
        quick_sort(pivot_index+1,right,arr)



