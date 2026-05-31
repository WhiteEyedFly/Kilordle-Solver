from collections import defaultdict
from ortools.sat.python import cp_model

with open("words.txt", "r") as f:
    words = f.read().splitlines()

with open("wordles.txt", "r") as f:
    wordles = f.read().splitlines()

positions = [set() for _ in range(5)]

for w in wordles:
    for pos, ch in enumerate(w):
        positions[pos].add(ch)

required = set()
for w in words:
    for pos, ch in enumerate(w):
        if ch in positions[pos]:
            required.add((pos, ch))

covers = defaultdict(list)

for i, w in enumerate(words):
    for pos, ch in enumerate(w):
        covers[(pos, ch)].append(i)

model = cp_model.CpModel()

x = [model.NewBoolVar("") for _ in range(len(words))]

for req in required:
    model.Add(sum(x[i] for i in covers[req]) >= 1)

model.Minimize(sum(x))

solver = cp_model.CpSolver()
status = solver.Solve(model)

chosen = [words[i] for i in range(len(words)) if solver.Value(x[i])]
print(f"Found solution in {len(chosen)} words")
print(chosen)