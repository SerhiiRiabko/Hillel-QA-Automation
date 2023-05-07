casino_blacklist = ["John Weak", "Elena Boscheva", "Jack Hardy", "Tommy Gun"]
poker_blacklist = ["Pablo Escobar", "Gustavo Ontario", "Alessandro Messo", "Cristian Lupen", "Cissilio Morano", "John Weak"]
alcohol_blacklist = ["Diego Maradona", "Fiordinant Eniesta", "Lionid Bukov", "Curt Cobain", "John Weak"]

everywhere_guys_black_list = set(casino_blacklist) & set(poker_blacklist) & set(alcohol_blacklist)
print(everywhere_guys_black_list)