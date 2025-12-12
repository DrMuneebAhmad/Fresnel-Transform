# Discrete Fresnel Transform (DFnT) and Inverse DFnT (IDFnT) in MATLAB and python

This repository contains MATLAB and python implementations of the Discrete Fresnel Transform (DFnT) and its inverse (IDFnT). These transforms are useful in various signal processing and optical applications.

## Discrete Fresnel Transform (DFnT)

The Discrete Fresnel Transform (DFnT) is used to model the propagation of waves and involves quadratic phase terms. It can be expressed mathematically as follows:

### Even \( N \)

For an even \( N \), the DFnT is given by:

\[
DFnT(x)_m = \frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} x_n \exp\left(\frac{j\pi}{N} (m - n)^2 - \frac{j\pi}{4}\right)
\]

### Odd \( N \)

For an odd \( N \), the DFnT is given by:

\[
DFnT(x)_m = \frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} x_n \exp\left(\frac{j\pi}{N} (m + 0.5 - n)^2 - \frac{j\pi}{4}\right)
\]

In these equations:
- \( x_n \) is the input signal.
- \( N \) is the length of the output signal.
- \( m \) and \( n \) are indices.
- \( j \) is the imaginary unit.

## Inverse Discrete Fresnel Transform (IDFnT)

The Inverse Discrete Fresnel Transform (IDFnT) is used to revert the DFnT back to the original signal. It can be expressed mathematically as follows:

### Even \( N \)

For an even \( N \), the IDFnT is given by:

\[
IDFnT(X)_n = \frac{1}{\sqrt{N}} \sum_{m=0}^{N-1} X_m \exp\left(-\frac{j\pi}{N} (m - n)^2 + \frac{j\pi}{4}\right)
\]

### Odd \( N \)

For an odd \( N \), the IDFnT is given by:

\[
IDFnT(X)_n = \frac{1}{\sqrt{N}} \sum_{m=0}^{N-1} X_m \exp\left(-\frac{j\pi}{N} (m - 0.5 - n)^2 + \frac{j\pi}{4}\right)
\]

In these equations:
- \( X_m \) is the transformed signal in the Fresnel domain.
- \( N \) is the length of the transformed signal.
- \( m \) and \( n \) are indices.
- \( j \) is the imaginary unit.


The DFnT and IDFnT are similar in structure to the Discrete Fourier Transform (DFT) and its inverse, but they incorporate quadratic phase factors. These phase factors make the DFnT particularly suitable for applications involving wave propagation and diffraction patterns.

## If you use the results or code from this repository in your research, please cite the following articles:

"O. D. W. (2004). Fresnel Transform and Its Applications. Journal of Optical Society".

"Ahmad M, Shin SY. A Comparative Performance Analysis of OCDM and OFDM for Wireless Communications. 한국통신학회 학술대회논문집. 2023 Jun:1380-1".
