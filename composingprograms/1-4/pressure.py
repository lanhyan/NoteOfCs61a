def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degree kelvin
    n -- particles of gas
    """
    k = 1.38e-23 #Boltzmann's constant
    return n * k * t / v
