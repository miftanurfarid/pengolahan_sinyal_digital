from scipy import signal
import matplotlib.pylab as plt
import numpy as np

fs = 8000
b = np.array([0.1871, 0.2, 0.1871])
w, h = signal.freqz(b)
plt.figure()
plt.title('Digital filter frequency response')
plt.subplot(211)
plt.plot(w*fs/(2*np.pi), 20 * np.log10(abs(h)), 'b')
plt.ylabel('Magnitude (dB)', color='b')
plt.xlabel('Frequency (Hz)')
plt.legend(['3-tap FIR'], loc='lower left')
plt.grid()
plt.show()
