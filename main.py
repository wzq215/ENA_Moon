import numpy as np
import spiceypy as spice
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


spice.furnsh('./kernels/naif0012.tls')
spice.furnsh('./kernels/pck00010.tpc')
spice.furnsh('./kernels/de440.bsp')
spice.furnsh('./kernels/moon_de440_220930.tf')
spice.furnsh('./kernels/moon_pa_de440_200625.bpc')
spice.furnsh('./kernels/moon_pa_de440_200625.cmt')

spice.furnsh('./kernels/moon_stations.cmt')
spice.furnsh('./kernels/moon_stations.tf')

def create_epoch(range_dt, step_td):
    beg_dt = range_dt[0]
    end_dt = range_dt[1]
    return [beg_dt + n * step_td for n in range((end_dt - beg_dt) // step_td)]

def get_body_pos(bodyName, epochDt, coord='IAU_SUN'):
    epochEt = spice.datetime2et(epochDt)
    bodyPos, _ = spice.spkpos(bodyName, epochEt, coord, 'NONE', 'SUN')
    return bodyPos

if __name__ == '__main__':
    et = spice.datetime2et(datetime(2024,2,27,12))
    J20002MSTN_arr = spice.sxform('J2000','MSTN-01_TOPO',et)
    J20002MOON_arr = spice.sxform('J2000','MOON_PA',et)
    print(J20002MSTN_arr)
    x_moon = np.dot(J20002MOON_arr[0:3, 0:3], [1, 0, 0])
    y_moon = np.dot(J20002MOON_arr[0:3, 0:3], [0, 1, 0])
    z_moon = np.dot(J20002MOON_arr[0:3, 0:3], [0, 0, 1])

    x_mstn = np.dot(J20002MSTN_arr[0:3, 0:3], [1, 0, 0])
    y_mstn = np.dot(J20002MSTN_arr[0:3, 0:3], [0, 1, 0])
    z_mstn = np.dot(J20002MSTN_arr[0:3, 0:3], [0, 0, 1])

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    ax.plot([0,1],[0,0],[0,0],'r')
    ax.plot([0,0],[0,2],[0,0],'r')
    ax.plot([0,0],[0,0],[0,3],'r')

    ax.plot([0, x_moon[0]], [0, x_moon[1]], [0, x_moon[2]], 'g')
    ax.plot([0, y_moon[0]*2.], [0, y_moon[1]*2.], [0, y_moon[2]*2.], 'g')
    ax.plot([0, z_moon[0]*3.], [0, z_moon[1]*3.], [0, z_moon[2]*3.], 'g')

    ax.plot([0, x_mstn[0]], [0, x_mstn[1]], [0, x_mstn[2]], 'b')
    ax.plot([0, y_mstn[0] * 2.], [0, y_mstn[1] * 2.], [0, y_mstn[2] * 2.], 'b')
    ax.plot([0, z_mstn[0] * 3.], [0, z_mstn[1] * 3.], [0, z_mstn[2] * 3.], 'b')

    ax.set_aspect('equal')

    ax.set_xlabel('X (J2000)')
    ax.set_ylabel('Y (J2000)')
    ax.set_zlabel('Z (J2000)')

    fig.show()


