import matplotlib.pyplot as plt
import numpy as np
import cv2
from datetime import datetime


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
    path to saved plot
    """
    # Get current time
    now = datetime.now()

    # Format as string
    time_string = now.strftime("%Y%m%d_%H%M%S")

    if len(arrays) > 2:
        rows = len(arrays) // 2
        cols = 2
        fig, axes = plt.subplots(rows, cols)
        fig.suptitle(title)

        images = []
        for i, arr in enumerate(arrays):
            row = i // cols
            col = i % cols

            images.append(axes[row, col].imshow(normalize(arr), cmap="jet"))
            axes[row, col].label_outer()
            axes[row, col].set_title(names[i])

        fig.colorbar(images[0], ax=axes, orientation="horizontal", fraction=0.1)

        # Save plot with time in filename
        plt.savefig(title + f"plot_{time_string}.png")
        return title + f"plot_{time_string}.png"
    elif len(arrays) == 2:
        fig, axes = plt.subplots(1, 2)
        fig.suptitle(title)

        images = []
        for i, arr in enumerate(arrays):
            images.append(axes[i].imshow(normalize(arr), cmap="jet"))
            axes[i].label_outer()
            axes[i].set_title(names[i])

        fig.colorbar(images[0], ax=axes, orientation="horizontal", fraction=0.1)

        # Save plot with time in filename
        plt.savefig(title + f"plot_{time_string}.png")
        return title + f"plot_{time_string}.png"

    else:
        # Display single image
        plt.imshow(arrays[0], cmap="jet")
        plt.title(title)
        plt.colorbar()

        # Save plot with time in filename
        plt.savefig(title + f"plot_{time_string}.png")
        return title + f"plot_{time_string}.png"