from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def bubble_sort_steps(arr):
    steps = []
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            steps.append(arr.copy())
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

def selection_sort_steps(arr):
    steps = []
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append(arr.copy())
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

def insertion_sort_steps(arr):
    steps = []
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            steps.append(arr.copy())
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps

def merge_sort_steps(arr):
    steps = []
    
    def merge_sort_helper(a, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        merge_sort_helper(a, l, mid)
        merge_sort_helper(a, mid + 1, r)
        merge(a, l, mid, r)

    def merge(a, l, m, r):
        left = a[l:m+1]
        right = a[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            steps.append(a.copy())
            k += 1
        while i < len(left):
            a[k] = left[i]
            steps.append(a.copy())
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            steps.append(a.copy())
            j += 1
            k += 1

    merge_sort_helper(arr.copy(), 0, len(arr) - 1)
    return steps

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    arr = data['array']
    algo = data['algorithm']

    if algo == 'bubble':
        steps = bubble_sort_steps(arr)
    elif algo == 'selection':
        steps = selection_sort_steps(arr)
    elif algo == 'insertion':
        steps = insertion_sort_steps(arr)
    elif algo == 'merge':
        steps = merge_sort_steps(arr)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400

    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)
