# State Description

Board size NxN
Cleaner 

# Inital State

Board(SIZE)

# Actions

* TAB

# Transition model

| Operator | Pre-conditions | Changes |
| -------- | -------------- | ------- |
| `tab(row, col)` | TO DO | TO DO |

# Goal State

```py
def goal(board):
	for row in board:
		for cellIsOn in row:
			if cellIsOn:
				return false
	return true
```

# Path Coast

* find diamond + 1
* find diamond in edge + 1
* clean + 1
