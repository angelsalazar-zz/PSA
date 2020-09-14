# State Description

Board size NxN

Set of tiles locations

Board Configuration

# Inital State

Board (N, N, ThingsToClean)

# Actions

* FIND_DIAMOND
* FIND_DIAMOND_IN_EDGE
* CLEAN

# Transition model

| Operator | Pre-conditions | Changes |
| -------- | -------------- | ------- |
| `findDiamond(row, col)` | TO DO | TO DO |
| `findDiamondInEdge(row, rol)` | TO DO | TO DO |

# Goal State

```py
def goal(board):
	for row in board:
		for cell in row:
			if cell:
				return false
	return true
```

# Path Coast

* find diamond + 1
* find diamond in edge + 1
* clean + 1
