# demonstrate stack implementation
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


#QUEUE
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

