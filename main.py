drivers = ["Khaled", "Medler", "Engram", "Carter", "Chiragg"]
bots = ["A", "B", "C", "D"]
max_rounds = (len(drivers) * len(bots)) // 4

rounds = [[["", ""], ["", ""], ["", ""], ["", ""]] for i in range(0, max_rounds)]

round_index = 0
round_index_counter = [0 for i in range(0, max_rounds)]
for d in drivers:
    for b in bots:
        rounds[round_index][round_index_counter[round_index]][0] = d
        rounds[round_index][round_index_counter[round_index]][1] = b
        round_index_counter[round_index] += 1
        round_index = (round_index + 1) % max_rounds

for r in rounds:
    print(r)

