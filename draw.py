#Draw PCA

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn

def Save_plot(fig, path):
    fig.savefig(path)

def typeof(x):
    print("{} | {}".format(x, type(x)))

def draw(DataFrame):

    c = np.array(DataFrame['PersonID'], dtype=np.int32)
    names = np.array(DataFrame['ImageID'], dtype=np.str)

    fig,ax = plt.subplots()
    sc = plt.scatter(np.array(DataFrame['PC1']),np.array(DataFrame['PC2']), 
                    c=c, 
                    s=10, 
                    cmap=cmap, 
                    #norm=norm
                    )

    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind):

        pos = sc.get_offsets()[ind["ind"][0]]

        annot.xy = pos
        text = "Label: {} \nPC1: {} \nPC2: {} ".format(names[ind["ind"]], pos[0], pos[1])
        annot.set_text(text)
        #annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_facecolor(cmap(128))
        annot.get_bbox_patch().set_alpha(.8)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()
    

PCA_Dataframe = pd.read_json('PCA.json', orient='records', dtype=False)
draw(PCA_Dataframe)
GT_PCA_Dataframe = pd.read_json('gt_pca.json', orient='records', dtype=False)
draw(GT_PCA_Dataframe)