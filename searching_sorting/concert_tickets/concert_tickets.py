from sys import stdin
from collections import deque


def print_price_paid(ticket_prices, customers):
    ticket_prices.sort()
    prices_list = deque(ticket_prices)
    for customer in customers:
        closest_index = find_closest_ticket(prices_list, customer)
        if closest_index == -1:
            print("-1")
        else:
            print(prices_list[closest_index])
            prices_list = []


def find_closest_ticket(ticket_prices, max_price):
    if not ticket_prices or ticket_prices[0] > max_price:
        return -1
    s, e = 0, len(ticket_prices) - 1

    while s < e:
        mid = -(-(s + e) // 2)
        if ticket_prices[mid] > max_price:
            e = mid - 1
        else:
            s = mid

    return s



if __name__ == '__main__':
    _ = stdin.readline()
    ticket_prices = [int(num) for num in stdin.readline().split()]
    customers = [int(num) for num in stdin.readline().split()]
    print_price_paid(ticket_prices, customers)