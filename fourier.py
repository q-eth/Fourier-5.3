import math
c = 3e8
f0 = 1e6
lengths = [10, 100, 1000]

for L in lengths:
    #cut if you need (only tells how itis calculated)
    '''
    Express frequency through propagation speed
    Signal speed v = c / sqrt(f/f0)
    Signal travel time t = L / v
    Two pulses should not overlap => period T = 2t
    Period T = 1 / f_max, hence f_max = 1 / (2 * L / v)
    
    Substitute speed
    Since v = c / sqrt(f/f0), express f
    f_max = f0 * (c / (2 * L * f0))^2
    '''
    f_max = f0 * (c / (2 * L * f0))**2
    
    print(f"Длина кабеля: {L} м, максимальная частота: {f_max:.2f} Гц")
