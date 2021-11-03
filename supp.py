import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def plotdb(X, y, clf, ax=None, plot_data=True, bool_colorbar=False, resolution=0.10, extra=0.10, lim=3.):

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = None 

    h = resolution
    
    
    xmin, ymin = np.min(X, axis=0)
    xmax, ymax = np.max(X, axis=0)
    
    xmin = -1.50
    xmax = 2.40
    ymin = -1
    ymax = 1.50
    xmax = ymax = lim
    xmin = ymin = -lim
    # extra = 0.50
    xx, yy = np.meshgrid(np.arange(xmin - extra, xmax + extra, h),
                         np.arange(ymin - extra, ymax + extra, h))

    cm = plt.cm.Blues
    cm_bright = mpl.colors.ListedColormap(['#FF0000', '#0000FF'])

    newx = np.c_[xx.ravel(), yy.ravel()]

    cm = plt.cm.RdYlBu


    newx = np.c_[xx.ravel(), yy.ravel()]
    Z = clf.predict(newx)
    Z = Z.reshape(xx.shape)
    contour_plot = ax.contourf(xx, yy, Z,
                               levels=20,
                               cmap=cm,
                               alpha=.2)
    if bool_colorbar:
        plt.colorbar(contour_plot, ax=ax)
    if plot_data:
        ax.scatter(X[:, 0], X[:, 1], c=y,
                    s=10,
                cmap=cm_bright,
                edgecolors='k',
                zorder=2)
    ax.grid(color='k',
            linestyle='-',
            linewidth=0.50,
            alpha=0.75)

    if fig is None:
        return fig, ax 
    return fig, ax

def sample(center, radius, n):
    def norm(v):
        return np.linalg.norm(v, ord=2, axis=1)
    d = center.shape[1]
    z = np.random.normal(0, 1, (n, d))
    u = np.random.uniform(0, radius**d, n)
    r = u**(1/float(d))
    z = np.array([a * b / c for a, b, c in zip(z, r,  norm(z))])
    z = z + center
    return z

def barchart_insert(coefs, ax, labels=None, hide=True):

    N = 2
    width = 0.9
    ind = np.arange(N)  # the x locations for the groups
    cmap = mpl.cm.get_cmap('tab10')
    ax.bar(ind + width, coefs, width, color=[cmap(2), cmap(4)])
    ax.set_xticks(ind + width)
    if hide:
        if labels:
            ax.set_xticklabels(labels)
        else:
            ax.set_xticklabels([])
            ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_linewidth(2)
    
    return ax