def file_bs() -> None:
    f_in = open("/home/ryanc/futhorcify/text_files/input.txt","rt")
    f_out = open("/home/ryanc/futhorcify/text_files/output.txt","wt")

    for line in f_in:
        f_out.write(line)

    f_in.close()
    f_out.close()