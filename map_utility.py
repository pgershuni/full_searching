def get_spn(toponym):
    uper_corner = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    lower_corner = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]

    delta_1 = str(abs(uper_corner[0] - lower_corner[0]))
    delta_2 = str(abs(uper_corner[1] - lower_corner[1]))

    return delta_1, delta_2