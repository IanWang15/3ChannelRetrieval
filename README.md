# Interpolation

In this project, the interpolation is an important component to retrieve the particle information. Several different interpolation python packages are tested.

## Scipy interpolate.interp1d

This class is considered legacy and will no longer receive updates. The difference is the x-coordinate sequence is expected to be increasing, but this is not explicitly enforced. In this project, the function of size to color ratio is not monotonic increasing.


## numpy.interp

The x-coordinate sequence is expected to be increasing. Even a sequence is monotonic decreasing is not allowed in this function.

## scipy.interpolate CubicSpline

x must be strictly increasing sequence.

