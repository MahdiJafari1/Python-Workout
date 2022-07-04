def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilenam, "w") as outfile:
        for one_line in infile:
            outfile.write(f"{one_line.rstrip()[::-1]}\n")
        