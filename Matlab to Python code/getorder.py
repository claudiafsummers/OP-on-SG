from junctionindex import junctionindex

def getorder():
    # helper function to reorder function value points from polydata_20.txt

    indices = []
    with open('indexorder', 'r') as f:
        for _ in range(3282):
            # Read until we hit the opening bracket
            ch = f.read(1)
            while ch != '[':
                ch = f.read(1)

            r = []
            ch = f.read(1)
            while ch != ']':
                if ch.strip() and ch not in ', ':
                    # Convert char to int, then add 1 (as in MATLAB str2num + 1)
                    r.append(int(ch) + 1)
                ch = f.read(1)

            indices.append(junctionindex(r, 7))

            # Read and discard 2 characters (comma, space or newline)
            f.read(2)

    return indices
