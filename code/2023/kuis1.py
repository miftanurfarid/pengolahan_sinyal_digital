import numpy as np

# xn sesuai dengan NIM: 0-421-033
xn = [3, 4, 2, 1, 0, 3]

for k in range(0, 6):
    x = []
    print(f"k = {k}\n")
    for n in range(0, 6):
        x.append(complex(np.round(np.cos(np.pi * n * k / 3), 2), np.round(np.sin(np.pi * n * k / 3), 2)) * xn[n])
    print(x)
    print("\n")
    print(np.sum(x))
    print("\n=====================\n")

print(np.round(np.fft.fft(xn), 2))
