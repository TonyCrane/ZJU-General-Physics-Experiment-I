import numpy as np

left1  = np.array([166*60+39, 165*60+52, 165*60+36, 166*60+24, 164*60+38, 165*60+49])
left2  = np.array([346*60+42, 345*60+54, 345*60+40, 346*60+27, 344*60+40, 345*60+53])
right1 = np.array([ 46*60+45,  45*60+59,  45*60+39,  46*60+29,  44*60+48,  45*60+58])
right2 = np.array([226*60+39, 225*60+55, 225*60+37, 226*60+27, 224*60+44, 225*60+55])

left1_right1 = np.abs(left1 - right1)
left2_right2 = np.abs(left2 - right2)
A = (left1_right1 + left2_right2) / 4
A_ = np.average(A)
uA = np.sqrt(sum((a - A_)**2 for a in A) / 30)
uB2 = 1 / 3
u = np.sqrt(uA**2 + uB2)

def print_ang(angle, end="\n"):
    print(f"{int(angle//60)}°{angle%60}'", end=end)

def print_anglst(lst):
    for angle in lst:
        print_ang(angle, " ")
    print()

print_anglst(left1_right1)
print_anglst(left2_right2)
print_anglst(A)
print_ang(A_)
print_ang(uA)
print_ang(u)

"""
119°54' 119°53' 119°57' 119°55' 119°50' 119°51' 
120°3' 119°59' 120°3' 120°0' 119°56' 119°58' 
59°59.25' 59°58.0' 60°0.0' 59°58.75' 59°56.5' 59°57.25' 
59°58.291666666666515' -> 59°58'
0°0.5300026205385948'
0°0.7837321679700987' -> 1'
"""