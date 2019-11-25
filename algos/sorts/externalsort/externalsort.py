def externalsort(infile_name, infile_size, page_size, ram_size, outfile_name):
    '''
    Args:
        file_name:    The name of the file to be read. Must be byte quadruples (ints).
        file_size:    The number of values in the file to sort. Must be integer
                      multiple of page_size.
        page_size:    The number of values that can be read from the file at
                      once.
        ram_size:     The number of values that can fit in ram at once.  ram_size
                      must be integer multiple of page_size.
        outfile_name: The name of the file to write the sorted data to.

    Raises:
        ValueError if file_size % page_size != 0 or ram_size % page_size != 0

    Returns:
        No return value. Writes the sorted data to outfile_name

    '''

    if file_size % page_size != 0 or file_size <= page_size or
            ram_size % page_size != 0 or ram_size <= page_size or
            file_size <= ram_size:
        s = 'file_size and ram_size must both be integer multiples of page_size'
        raise ValueError(s)

    # TODO
