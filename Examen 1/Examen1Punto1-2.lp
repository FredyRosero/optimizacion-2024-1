\ Model Problema de dieta
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  140 x[0] + 100 x[1]
Subject To
 c[0]: - 2500 x[0] - 2750 x[1] >= -2450
 c[1]: 2 x[0] + 3 x[1] >= 2
 c[2]: 200 x[0] + 20 x[1] >= 60
 c[3]: 200 x[0] + 200 x[1] >= 25
Bounds
End
