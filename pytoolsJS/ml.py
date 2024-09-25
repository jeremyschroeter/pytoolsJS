import numpy as np
import scipy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def kmeans(X: np.ndarray, n_clusters: int) -> np.ndarray:
    '''
    wrapper for quickly using Kmeans
    '''
    return KMeans(n_clusters=n_clusters).fit(X).labels_


def pca(X: np.ndarray, n_components: int) -> np.ndarray:
    '''
    wrapper for quickly using PCA
    '''
    return PCA(n_components=n_components).fit_transform(X)