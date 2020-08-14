import sys
import draw

if len(sys.argv) > 4:
    def f(x): return eval(sys.argv[1])
    draw.plot(f,
              float(sys.argv[2]),
              float(sys.argv[3]),
              float(sys.argv[4]))
else:
    print('Bad arguments')
