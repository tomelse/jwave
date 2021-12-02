from matplotlib import pyplot as plt
from jax import numpy as jnp


def is_numeric(x):
    """
    Check if x is a numeric value, including complex.
    """
    return isinstance(x, (int, float, complex))


def plot_complex_field(field: jnp.ndarray, figsize=(15, 8), max_intensity=None):
    """
    Plots a complex field.

    Args:
        field (jnp.ndarray): Complex field to plot.
        figsize (tuple): Figure size.
        max_intensity (float): Maximum intensity to plot.
            Defaults to the maximum value in the field.

    Returns:
        matplotlib.pyplot.figure: Figure object.
        matplotlib.pyplot.axes: Axes object.
    """
    fig, axes = plt.subplots(2, 1, figsize=figsize)

    if max_intensity is None:
        max_intensity = jnp.amax(jnp.abs(field))

    axes[0].imshow(field.real, vmin=-max_intensity, vmax=max_intensity, cmap="seismic")
    axes[0].set_title("Real wavefield")
    axes[1].imshow(jnp.abs(field), vmin=0, vmax=max_intensity, cmap="magma")
    axes[1].set_title("Wavefield magnitude")

    return fig, axes


def show_field(x, title="", vmax=None):
    plt.figure(figsize=(8, 6))
    maxval = vmax or jnp.amax(jnp.abs(x))
    plt.imshow(
        x,
        cmap="RdBu_r",
        vmin=-maxval,
        vmax=maxval,
        interpolation="nearest",
        aspect="auto",
    )
    plt.colorbar()
    plt.title(title)
    plt.axis("off")
    return None
