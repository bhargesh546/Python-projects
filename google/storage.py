"""
Question
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte 
will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. 
Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates 
the total number of bytes needed to store a file of a given size?
"""

def cal_storage(filesize):
    block_size = 4096

    blocks = filesize // block_size

    remaining_bytes = filesize % block_size

    if remaining_bytes > 0:
        return (blocks + 1) * block_size
    return blocks * block_size

print(cal_storage(1))
print(cal_storage(4097))
print(cal_storage(6000))