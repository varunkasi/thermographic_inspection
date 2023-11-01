import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cv2


def normalize(x: np.ndarray):
    """
    Normalizes a 2D array to values between 0 and 255

    Parameters
    ----------
    x : np.ndarray
        2D array to normalize

    Returns
    -------
    res : np.ndarray
        Normalized 2D array
    """
    res = np.zeros(x.shape)
    cv2.normalize(x, res, 0, 255, cv2.NORM_MINMAX)
    return res.astype("uint8")


def display(arrays: list[np.ndarray], names: list[str], title: str):
    """
    Takes in a list of 2D numpy arrays and displays them in a grid, with a colorbar

    Parameters
    ----------
    arrays : list
        List of numpy arrays to be displayed
    names : list
        List of names for each array
    title : str
        Title of the plot

    Returns
    -------
    None
    """
    fig, axes = plt.subplots(len(arrays), 1)
    fig.suptitle(title)

    images = []
    for i, arr in enumerate(arrays):
        images.append(axes[i].imshow(normalize(arr), cmap="jet"))
        axes[i].label_outer()
        axes[i].set_title(names[i])

    fig.colorbar(images[0], ax=axes, orientation="horizontal", fraction=0.1)

    plt.show()


if __name__ == "__main__":
    EOF1 = np.load("images/2023-09-12-15-left-straight-EOF1.npy")
    EOF2 = np.load("images/2023-09-12-15-left-straight-EOF2.npy")

    display([EOF1, EOF2])
