"""
"""

import sys

def velocity(vf = None, vi = None, a = None, t = None):
    """vf = vi + at"""
    """final velocity = initial velocity + acceleration * time"""
    if not _restrictNone(vf,vi,a,t):
        print("Input not properly provided")
        print("Expected: vf = vi + a * t")
        print("Received: {} = {} + {} * {}".format(vf,vi,a,t))
        sys.exit(1)
    ##decide what variable to return
    if not vf: ##solving for final velocity
        print("%%% vf = vi + a * t")
        print("%%% {} + {} * {}".format(vi,a,t))
        return vi + a * t
    elif not vi: ##solving for intial velocity
        print("%%% vi = vf - a * t")
        print("%%% {} - {} * {}".format(vf,a,t))
        return vf - a * t
    elif not a: ##solving for acceleration
        print("%%% a = (vf - vi) / t")
        print("%%% {} - {} * {}".format(vf,a,t))
        return (vf - vi) / t
    elif not t: ##solving for time
        print("%%% t = (vf - vi) / a")
        print("%%% {} - {} * {}".format(vf,a,t))
        return (vf - vi) / a
    else:
        print("Not sure how we made it here...")
        print("%%% vf = vi + a * t")
        print("%%% {} = {} + {} * {}".format(vf,vi,a,t))
        sys.exit(1)

def _restrictNone(*args):
    """confirm only one of the args is None"""
    totalNone = 0
    for arg in args:
        if arg is None:
            totalNone += 1
    return totalNone == 1

