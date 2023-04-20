import numpy as np
from PIL import Image
import time
from functools import reduce        # untuk faktor bilangan
import io
#from matplotlib import pyplot as plt


#OBE
def r_ij(m, row_i, row_j, r):
    return m[row_i] + r * m[row_j]


def swap(m, row_i, row_j):
    m[row_i], m[row_j] = m[row_j], m[row_i]


# logistic map sequence
def log_map(x0, n):
    x = x0
    for i in range(1000):
        x = 3.9 * x * (1 - x)  # 3.9 can be replaced with numbers in [3.7, 4]

    seq = np.zeros(n, dtype=np.uint8)
    for i in range(n):
        x = 3.9 * x * (1 - x)  # 3.9 can be replaced with numbers in [3.7, 4]
        seq[i] = x * 1000 % 256
    return seq


def generate_key(n, x0):
    # upper triangular matrix
    count = n * (n - 1) // 2
    seq = log_map(x0, count + n - 1)

    m = np.eye(n)

    idx = 0
    for i in range(n):
        for j in range(i + 1, n):
            m[i, j] = seq[idx]
            idx += 1

    for i in range(1, n):
        m[i] = r_ij(m, i, 0, seq[idx]) % 256
        idx += 1

    augmented = np.zeros((n, 2 * n))
    augmented[:, :n] = m
    augmented[:, n:] = np.eye(n)

    # OBE for obtaining the inverse
    # Lower-triangular matrix
    for col in range(n):
        for row in range(col + 1, n):
            augmented[row] = r_ij(augmented, row, col, -augmented[row, col]) % 256

    # Upper-triangular matrix
    for col in range(1, n):
        for row in range(col):
            augmented[row] = r_ij(augmented, row, col, -augmented[row, col]) % 256

    inverse = augmented[:, n:]

    return m, inverse


def encrypt(image_path, size, x0):
    start_time = time.time()
    
    # Load the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Generate the key
    key, inverse_key = generate_key(size, x0)
    
    # Reshape the image
    image_reshaped = image_array.reshape((size, image_array.size//size))
    
    # Multiply the key and the image
    multiplied = np.dot(key, image_reshaped) % 256
    
    # Reshape the cipher
    cipher = multiplied.reshape(image_array.shape).astype(np.uint8)
    
    # Save the cipher
    cipher_image = Image.fromarray(cipher)
    bytes_image = io.BytesIO()
    return cipher_image

def decrypt(gb, size, x0):
    print("Decryption process begin.")
    start_time = time.time()
    #gbku = Image.open(gb)
    mgb = np.array(gb)
    
    kunciku, balikku = generate_key(size, x0)
    
    mgb_reshape = mgb.reshape((size, mgb.size//size))
    
    m_kali = np.dot(balikku, mgb_reshape)%256
    m_decipher = m_kali.reshape(mgb.shape).astype(np.uint8)
    
    decipher = Image.fromarray(m_decipher)
    return decipher

def check_same(original_image, decrypted_image):
    gba = Image.open(original_image)
    gbd = Image.open(decrypted_image)
    
    mgba = np.array(gba)
    mgbd = np.array(gbd)
    
    if (mgba==mgbd).all():
        return "Both images are the same."
    else:
        return "Both images are different."


def factors(n):
    from functools import reduce
    fkt = set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    fkt_list = sorted(fkt)
    return [i for i in fkt_list if i < 1000]

if __name__ == '__main__':
    pass