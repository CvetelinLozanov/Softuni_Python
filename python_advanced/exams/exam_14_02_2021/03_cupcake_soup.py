from collections import deque


def stock_availability(boxes, command, *args):
    if command == 'delivery':
        for arg in args:
            boxes.append(arg)

    elif command == 'sell':
        if args:
            if isinstance(args[0], int):
                boxes = boxes[int(args[0]):]
            else:
                for product in args:
                    if product in boxes:
                        boxes = list(filter(lambda x: x != product, boxes))
        else:
            boxes = deque(boxes)
            boxes.popleft()
            boxes = list(boxes)

    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))