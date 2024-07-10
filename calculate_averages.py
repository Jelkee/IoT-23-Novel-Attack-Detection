import pandas as pd
import numpy as np
#CALCULATIONS FOR THE WEIGHTED AND NON WEIGTED AVERAGES
def weighted_average(data, weights):

    if len(data) != len(weights):
        raise ValueError("The lengths of data and weights must be the same.")

    weighted_sum = sum(data[i] * weights[i] for i in range(len(data)))
    total_weight = sum(weights)

    if total_weight == 0:
        raise ValueError("Total weight must be greater than zero to compute weighted average.")

    return weighted_sum / total_weight

accuracy = {
    "HGB": [0.3035, 0.3707, 0.9975, 0.7122, 0.9850, 0.9494, 0.9983, 0.3688, 0.9528],
    "RF": [0.5213, 0.4212, 0.9992, 0.7203, 0.9983, 0.8344, 0.9987, 0.9994, 0.4496],
    "SVM": [0.4377, 0.4694, 0.6924, 0.6549, 0.6847, 0.9369, 0.6950, 0.9519, 0.9487],
    "RNN": [0.6034, 0.9722, 0.9119, 0.9322, 0.9063, 0.9779, 0.8756, 0.9787, 0.4145],
    "MLP": [0.5185, 0.5240, 0.9473, 0.7470, 0.9383, 0.9431, 0.9585, 0.9920, 0.9836]
}

benign_accuracy = {
    "HGB": [0.9886, 0.9983, 0.9975, 0.9945, 0.9975, 0.9996, 0.9983, 0.9987, 0.9975],
    "RF": [0.9996, 0.9983, 0.9992, 0.9992, 0.9987, 0.9987, 0.9987, 0.9987, 0.9987],
    "SVM": [0.6072, 0.7100, 0.6906, 0.7073, 0.6906, 0.6022, 0.6906, 0.6906, 0.6873],
    "RNN": [0.8713, 0.8722, 0.9118, 0.8688, 0.9055, 0.8975, 0.8747, 0.8890, 0.9093],
    "MLP": [0.9591, 0.9582, 0.9473, 0.9582, 0.9473, 0.9489, 0.9582, 0.9582, 0.9582]
}

precision = {
    "HGB": [0.9812, 0.9980, 0.2500, 0.9980, 0.0000, 0.9999, 0.8182, 0.9986, 0.9993],
    "RF": [0.9998, 0.9984, 0.5000, 0.9997, 0.9063, 0.9996, 0.8571, 0.9997, 0.9990],
    "SVM": [0.8482, 0.8801, 0.0035, 0.9229, 0.0121, 0.9315, 0.0306, 0.9461, 0.9422],
    "RNN": [0.9465, 0.9684, 0.0095, 0.9682, 0.1146, 0.9762, 0.0571, 0.9744, 0.9268],
    "MLP": [0.9771, 0.9749, 0.0157, 0.9860, 0.0530, 0.9884, 0.1538, 0.9902, 0.9895]
}

recall = {
    "HGB": [0.1411, 0.1961, 1.0000, 0.6453, 0.0000, 0.9375, 1.0000, 0.2195, 0.8849],
    "RF": [0.4080, 0.2551, 1.0000, 0.6542, 0.9667, 0.7954, 1.0000, 0.9996, 0.2924],
    "SVM": [0.4063, 0.3919, 1.0000, 0.6449, 0.2333, 0.9986, 1.0000, 1.0000, 0.9999],
    "RNN": [0.5399, 0.9976, 1.0000, 0.9472, 0.9667, 0.9970, 1.0000, 1.0000, 0.2897],
    "MLP": [0.4141, 0.4134, 1.0000, 0.6970, 0.2333, 0.9417, 1.0000, 1.0000, 0.9900]
}

f1_score = {
    "HGB": [0.2467, 0.3278, 0.4000, 0.7838, 0.0000, 0.9677, 0.9000, 0.3599, 0.9386],
    "RF": [0.5795, 0.4064, 0.6667, 0.7840, 0.9355, 0.8859, 0.9231, 0.9996, 0.4524],
    "SVM": [0.5494, 0.5423, 0.0070, 0.7593, 0.0230, 0.9639, 0.0594, 0.9723, 0.9702],
    "RNN": [0.6876, 0.9828, 0.0188, 0.9576, 0.2049, 0.9865, 0.1080, 0.9870, 0.4414],
    "MLP": [0.5817, 0.5806, 0.0309, 0.8167, 0.0864, 0.9645, 0.2666, 0.9951, 0.9897]
}

weights = [10000, 10000, 2, 10000, 30, 10000, 18, 10000, 9398]

accuracy_df = pd.DataFrame(accuracy)
benign_accuracy_df = pd.DataFrame(benign_accuracy)
precision_df = pd.DataFrame(precision)
recall_df = pd.DataFrame(recall)
f1_score_df = pd.DataFrame(f1_score)

average_accuracy = np.average(accuracy_df, axis=0)
average_benign_accuracy = np.average(benign_accuracy_df, axis=0)
average_precision = np.average(precision_df, axis=0)
average_recall = np.average(recall_df, axis=0)
average_f1_score = np.average(f1_score_df, axis=0)

weighted_accuracy = np.average(accuracy_df, weights=weights, axis=0)
weighted_benign_accuracy = np.average(benign_accuracy_df, weights=weights, axis=0)
weighted_precision = np.average(precision_df, weights=weights, axis=0)
weighted_recall = np.average(recall_df, weights=weights, axis=0)
weighted_f1_score = np.average(f1_score_df, weights=weights, axis=0)

print(average_accuracy)
print(average_benign_accuracy)
print(average_precision)
print(average_recall)
print(average_f1_score)
print("____________________")
print(weighted_accuracy)
print(weighted_benign_accuracy)
print(weighted_precision)
print(weighted_recall)
print(weighted_f1_score)


