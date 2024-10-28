#pool_ops code
import sys
import math

if len(sys.argv)==8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

h_out = math.floor((h_in + 2*p - h_pool)/s + 1)
w_out = math.floor((w_in + 2*p - w_pool)/s + 1)

c_out = c_in

adds = h_out*w_out*c_in*(h_pool*w_pool - 1)
muls = 0
divs = c_in*h_out*w_out

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
