#Write a program to solve a fractional Knapsack problem using a greedy method

def fractional_knapsack(weights, values, capacity):
    res=0
    for pair in sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True):
        if capacity <= 0:
            break
        if pair[0]> capacity:
            res+= int(capacity * (pair[1]/pair[0]))
            capacity=0
        elif pair[0]< capacity:
            res += pair[1]
            capacity-= pair[0]
    print(f"Maximum value of knapsack: {res}")

def knapsack_menu():
    weights=[]
    values=[]
    capacity= int(input("enter capacity: "))
    n= int(input("how many values to enter: "))
    for i in range(n):
        w=int(input("enter weights: "))
        v=int(input("enter values: "))
        weights.append(w)
        values.append(v)
    print(weights)
    print(values)
    fractional_knapsack(weights, values, capacity)

if __name__=="__main__":
    knapsack_menu()