from sys import stdin
import heapq

# Getting TLE, this is a solid solution though, implement in C++

def min_room_allocation(customers):
    customers.sort()
    customer_bookings = [-1 for _ in range(len(customers) // 2)]
    rooms = [i + 1 for i in range(len(customers) // 2)]
    for customer in customers:
        if customer[1] == 'A':
            room = heapq.heappop(rooms)
            customer_bookings[customer[2]] = room
        else:
            heapq.heappush(rooms, customer_bookings[customer[2]])
    print(max(customer_bookings))
    print(' '.join([str(booking) for booking in customer_bookings]))

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    n = read_num()
    customers = []
    for i in range(n):
        arrival, departure = read_nums()
        customers.append(
            (arrival, 'A', i)
        )
        customers.append(
            (departure, 'D', i)
        )
    min_room_allocation(customers)