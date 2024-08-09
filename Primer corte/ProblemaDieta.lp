\ Model Problema de dieta
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  50 x_i[0] + 20 x_i[1] + 30 x_i[2] + 80 x_i[3]
Subject To
 c[0]: 400 x_i[0] + 200 x_i[1] + 150 x_i[2] + 500 x_i[3] - x_i[4] = 500
 c[1]: 3 x_i[0] + 2 x_i[1] - x_i[5] = 6
 c[2]: 2 x_i[0] + 2 x_i[1] + 4 x_i[2] + 4 x_i[3] - x_i[6] = 10
 c[3]: 2 x_i[0] + 4 x_i[1] + x_i[2] + 5 x_i[3] - x_i[7] = 8
Bounds
End
