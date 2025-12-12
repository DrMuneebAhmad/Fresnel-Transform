# Colin GUIRARDEL
# Adapted the work from Muneeb Ahmad from matlab to python


##
import numpy as np

##
exp = np.exp
sqrt = np.sqrt

pi = np.pi
j = 1j
exp_neg_j_pi_over_4 = exp(-j * pi / 4)
exp_j_pi_over_4 = exp(j * pi / 4)
##

def DFT(input_signal, N = None, dtype = np.complex64):

    # Ensure the input_signal is a column vector, and that dtype accepts complex values
    input_signal = np.array(input_signal,dtype = dtype)
    initial_shape = input_signal.shape
    input_signal = input_signal.reshape(-1, 1)


    # Determine the value of N
    if N is None :
        N = np.size(input_signal)


    # Precompute constants
    sqrtN = sqrt(N)
    pi_over_N = pi / N

    # Constructing the DFnT matrix
    dFnT_matrix = np.zeros((N, np.size(input_signal)), dtype = np.complex64);
    for m in range(N):
        for n in range(np.size(input_signal)):
            if N % 2 == 0 : # For even N
                phase = pi_over_N * (m - n)**2
            else : # For odd N
                phase = pi_over_N * (m + 0.5 - n)**2
            dFnT_matrix[m, n] = (1 / sqrtN) * exp_neg_j_pi_over_4 * exp(1j * phase);

    # Applying the DFnT

    dFnT_output = dFnT_matrix @ input_signal

    # restore original shape

    dFnT_output = dFnT_output.reshape(initial_shape)
    return dFnT_output


def IDFT(input_signal, N = None, dtype = np.complex64):
    # Ensure the input_signal is a column vector, and that dtype accepts complex values
    input_signal = np.array(input_signal,dtype = dtype)
    initial_shape = input_signal.shape
    input_signal = input_signal.reshape(-1, 1)

    # Determine the value of N
    if N is None :
        N = np.size(input_signal)


    # Precompute constants
    sqrtN = sqrt(N)
    pi_over_N = pi / N


    # Constructing the iDFnT matrix
    idFnT_matrix = np.zeros((N, np.size(input_signal)), dtype = np.complex64);
    for m in range(N):
        for n in range(np.size(input_signal)):
            if N % 2 == 0 : # % For even N
                phase = pi_over_N * (m - n)**2
            else : # For odd N
                phase = pi_over_N * (m - 0.5 - n)**2  # sign was changed from +.5 to - .5 for better result with odd numbers
            idFnT_matrix[m, n] = (1 / sqrtN) * exp_j_pi_over_4 * exp(-1j * phase);

    # Applying the DFnT

    idFnT_output = idFnT_matrix @ input_signal

    # restore original shape
    idFnT_output = idFnT_output.reshape(initial_shape)
    return idFnT_output

## Field to Intensity
def E2I(E):
    return abs(E)**2


## tests

if __name__ == '__main__':


    import matplotlib.pyplot as plt

    # define a few arrays
    x = np.linspace(-5,5,100)
    gauss = exp(-x**2)
    rect = (-.5 <= x) & (x < .5)
    rect = rect.astype(np.float64)

    for signal in [gauss, rect] :

        dft = DFT(signal)
        idft = IDFT(dft)
        error = E2I(signal - idft) # Error in Intensity
        maxerr = error.max()

        fig = plt.figure()
        ax1 = plt.subplot(2,1,1)
        ax1.plot(x,E2I(signal),label = 'input signal')
        ax1.plot(x,E2I(idft),label = f'idft(dft), max error={maxerr:.1e}')
        ax1.set_ylabel("I = |E|**2")
        ax1.legend()

        ax2 = plt.subplot(2,1,2)
        ax2.plot(x,E2I(dft),label = 'dft')
        ax2.set_ylabel("I = |E|**2")
        ax2.legend()
    plt.show()