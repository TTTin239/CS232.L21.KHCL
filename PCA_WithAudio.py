# Trần Trung Tín - 19522351
from IPython.display import Audio
from scipy.io import wavfile
from sklearn.decomposition import PCA
import numpy as np
from bz2 import compress
import pandas as pd

samplerate, tabulasa = wavfile.read('31072 (mp3cut.net).wav')

start = samplerate * 14 
end = start + samplerate * 10 
Audio(data=tabulasa[start:end, 0], rate=samplerate)

def pca_reduce(signal, n_components, block_size=1024):
    samples = len(signal)
    hanging = block_size - np.mod(samples, block_size)
    padded = np.lib.pad(signal, (0, hanging), 'constant', constant_values=0)
    reshaped = padded.reshape((len(padded) // block_size, block_size))
    pca = PCA(n_components=n_components)
    pca.fit(reshaped)  
    transformed = pca.transform(reshaped)
    reconstructed = pca.inverse_transform(transformed).reshape((len(padded)))
    return pca, transformed, reconstructed

tabulasa_left = tabulasa[:,0]

_, _, reconstructed = pca_reduce(tabulasa_left, 1024, 1024)

Audio(data=reconstructed[start:end], rate=samplerate)

_, _, reconstructed = pca_reduce(tabulasa_left, 32, 1024)

Audio(data=reconstructed[start:end], rate=samplerate)

def raw_estimate(transformed, pca):
    signal_bytes = transformed.tobytes()
    component_bytes = transformed.tobytes()
    return (len(signal_bytes) + len(component_bytes)) / (2**20)

def bz2_estimate(transformed, pca):
    bytestring = transformed.tobytes() + b';' + pca.components_.tobytes()
    compressed = compress(bytestring)
    return len(compressed) / (2**20)

compression_attempts = [
    (1, 1),
    (1, 2),
    (1, 4),
    (4, 32),
    (16, 256),
    (32, 256),
    (64, 256),
    (128, 1024),
    (256, 1024),
    (512, 1024),
    (128, 2048),
    (256, 2048),
    (512, 2048),
    (1024, 2048)
]

def build_estimates(signal, n_components, block_size):
    pca, transformed, recon = pca_reduce(tabulasa_left, n_components, block_size)
    raw_pca_estimate = raw_estimate(transformed, pca)
    bz2_pca_estimate = bz2_estimate(transformed, pca)
    raw_size = len(recon.tobytes()) / (2**20)
    return raw_size, raw_pca_estimate, bz2_pca_estimate

pca_compression_results = pd.DataFrame([
        build_estimates(tabulasa_left, n, bs)
        for n, bs in compression_attempts
    ])

pca_compression_results.columns = ["Raw", "PCA", "PCA w/ BZ2"]
pca_compression_results.index = compression_attempts
pca_compression_results