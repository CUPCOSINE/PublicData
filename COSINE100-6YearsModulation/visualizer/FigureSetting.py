import numpy as np
import cmasher as cmr
import matplotlib.pyplot as plt

mm_to_inches = 1.0 / 25.4


def set_nature_style():
    font = "Arial"
    fontsize = {
        "normal": 6,
        "large": 7,
        "small": 5,
    }
    dpi = 450

    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["ps.fonttype"] = 42
    plt.rcParams["font.family"] = font
    plt.rcParams["font.size"] = fontsize["normal"]

    plt.rcParams["figure.labelsize"] = fontsize["normal"]
    plt.rcParams["axes.labelsize"] = fontsize["normal"]
    plt.rcParams["axes.titlesize"] = fontsize["large"]
    plt.rcParams["xtick.labelsize"] = fontsize["normal"]
    plt.rcParams["ytick.labelsize"] = fontsize["normal"]
    plt.rcParams["legend.fontsize"] = fontsize["normal"]

    plt.rcParams["image.cmap"] = "cmr.ocean_r"

    plt.rcParams["xtick.major.width"] = 0.5
    plt.rcParams["ytick.major.width"] = 0.5
    plt.rcParams["xtick.minor.width"] = 0.5
    plt.rcParams["ytick.minor.width"] = 0.5

    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"

    plt.rcParams["xtick.major.size"] = 3
    plt.rcParams["ytick.major.size"] = 3
    plt.rcParams["xtick.minor.size"] = 1.5
    plt.rcParams["ytick.minor.size"] = 1.5

    plt.rcParams["axes.linewidth"] = 0.5

    plt.rcParams["lines.linewidth"] = 0.5
    plt.rcParams["lines.markersize"] = 2

    plt.rcParams["figure.dpi"] = dpi
    plt.rcParams["savefig.dpi"] = dpi
    plt.rcParams["savefig.format"] = "pdf"
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["savefig.pad_inches"] = 0.05
    plt.rcParams["savefig.transparent"] = True

    plt.rcParams["axes.unicode_minus"] = False


# color palette
colors = {
    "IbsRed": "#CC1400",  # IBS Red
    "IbsBrown": "#B18D4F",  # IBS Brown
    "IbsGrey": "#666466",  # IBS Grey
    "IbsLightGrey": "#999999",  # IBS Light Grey
    "InfnDeepBlue": "#002D4B",  # INFN Deep Blue
    "InfnBlue": "#4297B4",  # INFN-LNGS SkyBlue
    "Yellow": "#FFFF66",  # Just yellow, which is distinguishable from cmap
}

def color_blur(color_hex, alpha=0.1):
    color = np.array([int(color_hex[i:i+2], 16) for i in (1, 3, 5)])
    color = color / 255
    color = alpha * color + (1 - alpha) * np.array([1, 1, 1])
    return color

