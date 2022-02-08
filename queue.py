def create_que(num, value):
    stack = Stack(6)
    output_queue = Queue(6)
    while (value <= num):
        stack.push(num + value)
        temp_stack = Stack(stack.get_max_size())
        while (not stack.is_empty()):
            temp_stack.push(stack.pop() * 2)
        num = num - value
        value += 2
        if(not temp_stack.is_empty()):
            output_queue.enqueue(temp_stack.pop())
    return output_queue