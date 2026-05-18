import numpy as np
import pandas
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":

    # get arguments
    parser = argparse.ArgumentParser(description = "Bar graph generator args parser")

    parser.add_argument(
        "--data-src-filename",
        type = str,
        required = True,
        help = "Source data filename"
    )

    parser.add_argument(
        "--graph-filename",
        type = str,
        required = True,
        help = "Graph filename"
    )

    parser.add_argument(
        "--method",
        type = str,
        required = True,
        help = "Method name"
    )

    parser.add_argument(
        "--noise-std",
        type = float,
        default = None,
        help = "Gaussian noise std"
    )

    parser.add_argument(
        "--metric",
        type = str,
        choices = ["mean", "std"],
        default = "mean",
        help = "Metric to plot: 'mean' for Absolute error mean, 'std' for Absolute error std. deviation"
    )

    args = parser.parse_args()

    metric_column = "Normalized error mean" if args.metric == "mean" else "Normalized error std. deviation"
    metric_label = "Normalizuotos paklaidos vidurkis" if args.metric == "mean" else "Normalizuotos paklaidos standartinis nuokrypis"

    color_map = {
        ("mean", True):  "coral",
        ("mean", False): "steelblue",
        ("std",  True):  "#DBC2CF",
        ("std",  False): "#9FA2B2",
    }
    edge_color = color_map.get((args.metric, args.noise_std == 0), "gray")

    # hatch patterns per benchmark function — dots, dense dots, circles
    hatch_patterns = [None,  "..", "//"]

    # get data
    data_frame = pandas.read_csv(args.data_src_filename)
    data_frame.columns = data_frame.columns.str.strip()
    data_frame = data_frame.sort_values(by=["Method", "Data function", "Noise std. deviation", "Data size"]).reset_index(drop = True)

    # prepare labels
    benchmark_funcs = ["sphere_func", "rosenbrock_func", "rastrigin_func"]
    benchmark_func_names = ["Sferos funkcija", "Rozenbroko funkcija", "Rastrigino funkcija"]

    data_sizes = ["1 tūkst. taškų", "10 tūkst. taškų", "100 tūkst. taškų", "1 mln. taškų", "10 mln. taškų"]

    x = np.arange(len(data_sizes))
    width = .6 / len(benchmark_funcs)

    fig, method_axis = plt.subplots(figsize=(12, 7))

    for i, (func, hatch) in enumerate(zip(benchmark_funcs, hatch_patterns)):
        filtered = data_frame[
            (data_frame["Method"] == args.method) &
            (data_frame["Noise std. deviation"] == args.noise_std) &
            (data_frame["Data function"] == func)
        ]

        offset = (i - len(benchmark_funcs) / 2 + 0.5) * width
        method_axis.bar(
            x + offset,
            filtered[metric_column].values,
            width = width,
            facecolor = edge_color,
            edgecolor = "white",
            hatch = hatch,
            linewidth = 1.5,
            alpha = 1,
            label = benchmark_func_names[i]
        )

    # primary x-axis — data sizes only
    method_axis.set_xticks(x)
    method_axis.set_xticklabels(data_sizes, fontsize = 10)
    method_axis.set_xlabel("Taškų kiekis duomenų aibėje", labelpad = 15, fontsize = 12)

    # y-axis configuration
    method_axis.set_ylabel(metric_label, labelpad = 15, fontsize = 12)
    method_axis.grid(axis = 'y', linestyle = '--', alpha = 0.5)

    method_axis.legend(fontsize = 10)

    plt.tight_layout()
    plt.savefig(args.graph_filename)