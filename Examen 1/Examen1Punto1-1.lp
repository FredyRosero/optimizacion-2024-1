\ Model Problema de dieta
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  140 x[0] + 100 x[1]
Subject To
 R0: 2 x[0] + 3 x[1] >= 2
 R1: 200 x[0] + 20 x[1] >= 60
 R2: 200 x[0] + 200 x[1] >= 25
 R3: 2500 x[0] + 2750 x[1] <= 2450
Bounds
End
