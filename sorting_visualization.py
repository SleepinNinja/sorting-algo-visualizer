import tkinter
import random

arr = []
value, size, space, width = 0, 0, 0, 0

def get_value():
	global value, size, space, width
	value = check_value.get()

	if value in [1,3,7]:
		size, space, width = 150, 8, 3

	else:
		size, space, width = 700, 1, 1

def start():
	shuffle_arr()

	if value == 1:
		bubble_sort(arr)

	elif value == 2:
		merge_sort(arr, 0, len(arr) - 1)

	elif value == 3:
		insertion_sort(arr)

	elif value == 4:
		selection_sort(arr)

	elif value == 5:
		quick_sort(arr, 0, len(arr) - 1)

	elif value == 6:
		improved_selection_sort(arr)

	elif value == 7:
		cocktail_sort(arr)

def shuffle_arr():
	clear_lines()
	global arr
	arr = [random.randint(5, 595) for _ in range(size)]
	random.shuffle(arr)

	for i in range(len(arr)):
		draw_lines(arr, i, "red")

def draw_lines(arr,i, color):
	canvas.create_line(i + i * space , 600, i + i * space , 600 - arr[i], fill = color, width = width)
	root.update()


def white_line(k):
	canvas.create_line(k + k * space, 600, k + k * space, 0, fill = "white", width = width)
	root.update()


def clear_lines():
	canvas.delete('all')


def bubble_sort(arr):
	for i in range(len(arr)):
		already_sorted = True
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				white_line(j)
				white_line(j + 1)

				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				already_sorted = False

				draw_lines(arr, j, "red")
				draw_lines(arr, j+1, "red")

def merge_sort(arr, left, right):
	if left < right:
		middle = (left + (right - 1)) // 2
		merge_sort(arr, left, middle)
		merge_sort(arr, middle + 1, right)
		merge(arr, left, middle, right)


def merge(arr, left, middle, right):
	n1 = middle - left + 1
	n2 = right - middle

	left_array = [0] * n1
	right_array = [0] * n2

	for i in range(n1):
		left_array[i] = arr[i + left]

	for j in range(n2):
		right_array[j] = arr[middle + j + 1]

	i = 0
	j = 0
	k = left

	while i < n1 and j < n2:
		if left_array[i] <= right_array[j]:
			white_line(k)
			arr[k] = left_array[i]
			draw_lines(arr, k, "red")
			i += 1

		else:
			white_line(k)
			arr[k] = right_array[j]
			draw_lines(arr, k, "red")
			j += 1

		k += 1

	while i < n1:
		white_line(k)
		arr[k] = left_array[i]
		draw_lines(arr, k, "red")
		i += 1
		k += 1

	while j < n2:
		white_line(k)
		arr[k] = right_array[j]
		draw_lines(arr, k, "red")
		j += 1
		k += 1

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			white_line(j)
			arr[j + 1] = arr[j]
			draw_lines(arr, j, "red")
			j -= 1

		white_line(i)
		arr[j + 1] = key
		draw_lines(arr, j + 1, "red")


def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i

		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_index]:
				white_line(j)
				white_line(min_index)
				min_index = j

		arr[i], arr[min_index] = arr[min_index], arr[i]
		draw_lines(arr, i, "red")
		draw_lines(arr, min_index, "red")


def quick_sort(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partition(arr, low, high)
		quick_sort(arr, low, pi - 1)
		quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
	i = low
	piviot = arr[high]

	for j in range(low, high):
		if arr[j] <= piviot:
			white_line(i)
			white_line(j)
			arr[i], arr[j] = arr[j], arr[i]
			draw_lines(arr, i, "red")
			draw_lines(arr, j, "red")
			i += 1

	white_line(i)
	white_line(high)
	arr[i], arr[high] = arr[high], arr[i]
	draw_lines(arr, i, "red")
	draw_lines(arr, high, "red")
	return i


def improved_selection_sort(arr):
	start = 0
	end = len(arr) - 1
	while start - end != 1 and start != end:
		smallest_index, largest_index = start, start
		for i in range(start, end + 1):
			if arr[i] <= arr[smallest_index]:
				smallest_index = i

			elif arr[i] >= arr[largest_index]:
				largest_index = i

		large_value = arr[largest_index]

		if largest_index == start:
			largest_index = smallest_index

		white_line(start)
		white_line(smallest_index)
		arr[start], arr[smallest_index] = arr[smallest_index], arr[start]
		draw_lines(arr, start, "red")
		draw_lines(arr, end, "red")

		if arr[end] != large_value:
			white_line(end)
			white_line(largest_index)
			arr[end], arr[largest_index] = arr[largest_index], arr[end]
			draw_lines(arr, end, "red")
			draw_lines(arr, largest_index, "red")

		start += 1
		end -= 1

def cocktail_sort(arr):
	for i in range(len(arr)):
		swapped = True

		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				white_line(j)
				white_line(j + 1)
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
				draw_lines(arr, j, "red")
				draw_lines(arr, j + 1, "red")

		if not swapped:
			break

		for k in range(len(arr) - i - 1, 0, -1):
			if arr[k - 1] > arr[k]:
				white_line(k - 1)
				white_line(k)
				arr[k - 1], arr[k] = arr[k], arr[k - 1]
				swapped = True
				draw_lines(arr, k - 1, "red")
				draw_lines(arr, k, "red")

		if not swapped:
			break


root = tkinter.Tk()
canvas = tkinter.Canvas(root, height = 600, width = 1400, bg = "white")
canvas.pack()
check_value = tkinter.IntVar()

l1 = tkinter.Label(root, text = "Select algorithm  ")
l1.pack(side = tkinter.LEFT)
r1 = tkinter.Radiobutton(root, variable = check_value, value = 1, text = "Bubble Sort", command = get_value)
r2 = tkinter.Radiobutton(root, variable = check_value, value = 2, text = "Merge Sort", command = get_value)
r3 = tkinter.Radiobutton(root, variable = check_value, value = 3, text = "Insertion Sort", command = get_value)
r4 = tkinter.Radiobutton(root, variable = check_value, value = 4, text = "Selection Sort", command = get_value)
r5 = tkinter.Radiobutton(root, variable = check_value, value = 5, text = "Quick Sort", command = get_value)
r6 = tkinter.Radiobutton(root, variable = check_value, value = 6, text = "Improved Selection Sort", command = get_value)
r7 = tkinter.Radiobutton(root, variable = check_value, value = 7, text = "Cocktail Sort", command = get_value)
r1.pack(side = tkinter.LEFT)
r2.pack(side = tkinter.LEFT)
r3.pack(side = tkinter.LEFT)
r4.pack(side = tkinter.LEFT)
r5.pack(side = tkinter.LEFT)
r6.pack(side = tkinter.LEFT)
r7.pack(side = tkinter.LEFT)

b2 = tkinter.Button(root, text = "Start Sorting", justify = tkinter.CENTER, command = start)
b2.pack(side = tkinter.RIGHT)
root.mainloop()
