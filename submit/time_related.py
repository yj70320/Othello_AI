import resource

def get_time():
    rs = resource.getrusage(resource.RUSAGE_SELF)
    return rs[0] + rs[1]