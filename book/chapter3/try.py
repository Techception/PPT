friends = ['praj', 'radi', 'kev']
print(friends[0])
print(friends[1])
print(friends[2])


message = f"Hello '{friends[0].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[1].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[2].title()}' whats the plan?"
print(message)

vehicles = ['car','bus','train','motorbike','plane']
stmnts = [
        f'I would like to {vehicles[1]} a nut',
        f'I would runa a {vehicles[2]} on that',
        f'wont catch me dead on a {vehicles[3]}',
        f'are you "Higher than a {vehicles[-1]}"?',
        f'faster by {vehicles[0]}'
        ]
for i in stmnts:
    print(i)

