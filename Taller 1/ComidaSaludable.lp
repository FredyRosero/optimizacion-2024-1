\ Model Comida Saludable
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  1.56 x_ij[0,0] + 1.186 x_ij[0,1] - 811.3 x_ij[0,2] + 0.53 x_ij[1,0]
   + 0.156 x_ij[1,1] - 812.33 x_ij[1,2] + 0.13 x_ij[2,0] - 0.244 x_ij[2,1]
   - 812.73 x_ij[2,2]
Subject To
 R0: - 0.6 x_ij[0,0] + 0.4 x_ij[0,1] - 0.6 x_ij[0,2] >= 0
 R1: - 0.25 x_ij[0,0] - 0.25 x_ij[0,1] + 0.75 x_ij[0,2] <= 0
 R2: 0.4 x_ij[1,0] - 0.6 x_ij[1,1] - 0.6 x_ij[1,2] >= 0
 R3: 0.8 x_ij[2,0] - 0.2 x_ij[2,1] - 0.2 x_ij[2,2] <= 0
 R4: - 0.6 x_ij[2,0] - 0.6 x_ij[2,1] + 0.4 x_ij[2,2] >= 0
 R5: x_ij[0,0] + x_ij[1,0] + x_ij[2,0] <= 100
 R6: x_ij[0,1] + x_ij[1,1] + x_ij[2,1] <= 80
 R7: x_ij[0,2] + x_ij[1,2] + x_ij[2,2] <= 60
Bounds
End
