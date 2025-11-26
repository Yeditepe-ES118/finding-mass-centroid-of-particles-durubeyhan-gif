import numpy as np
def centroid(p1x,p1y,p2x,p2y,p3x,p3y,m1,m2,m3):
    positions= np.array([[p1x,p2x,p3x], [p1y,p2y,p3y]])
    mass= np.array([m1,m2,m3])
    
    cx= np.sum(positions[0,:]*mass)/ np.sum(mass) # * elementwise multiplication
    cy= np.sum(positions[1,:]*mass)/np.sum(mass)
    tot_mass= np.sum(mass)
    
    return cx, cy, tot_mass
#ilk olarak pozisyonları tanımlıyoruz
#istediğin yerde durmak için kırmızı noktayı işaretle ve debug file ile kodu çalıştır
#cx= p1xm1+p2xm2+p3xm3/m1+m2+m3
# [0,:] birinci satır anlamına geliyor
