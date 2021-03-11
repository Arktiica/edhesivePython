def swap(arr, in1, in2):
   w = arr[in1]
   arr[in1] = arr[in2]
   arr[in2] = w

terms = ["Bandwidth", "Hierarchy", "IPv6", "Software", "Firewall", "Cybersecurity", "Lists", "Program", "Logic","Reliability"]

print(terms)
swap(terms, 5, 1)
swap(terms, 2, 4)
swap(terms, 3, 5)
swap(terms, 5, 6)
swap(terms, 6, 8)
swap(terms, 8, 9)
print(terms)
