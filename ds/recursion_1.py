def TOH(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print ("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    # print(n)
    # count= count+1
    TOH(n - 1, from_rod, aux_rod, to_rod)
    # print(n)
    print( "Move disk", n, "from rod", from_rod, "to rod", to_rod)
    # print(n)
    TOH(n - 1, aux_rod, to_rod, from_rod)
    # print(n)


# Driver code
# n = int(input("Enter the no. of disk"))
TOH(3, 'A', 'C', 'B')
# A, C, B are the name of rods


