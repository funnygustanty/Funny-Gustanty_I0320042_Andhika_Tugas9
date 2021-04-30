import array

# mengonversi string ke dalam array.array
B = array.array('c')
B.fromstring("python")
for karakter in B:
    print("%c " % karakter, end="")