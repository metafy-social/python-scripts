The function makes a labelled confusion matrix comparing predictions and ground truth labels.
  
If classes is passed, confusion matrix will be labelled, if not, integer class values will be used.

Args:

* `y_true`: Array of truth labels (must be same shape as y_pred).
* `y_pred`: Array of predicted labels (must be same shape as y_true).
* `classes`: Array of class labels (e.g. string form). If `None`, integer labels are used.
* `figsize`: Size of output figure (default=(10, 10)).
* `text_size`: Size of output figure text (default=15).
* `norm`: normalize values or not (default=False).
* `savefig`: save confusion matrix to file (default=False).

Returns: A labelled confusion matrix plot comparing y_true and y_pred.

### Example usage:

> """make_confusion_matrix(y_true=test_labels, # ground truth test labels
                        y_pred=y_preds, # predicted labels
                        classes=class_names, # array of class label names
                        figsize=(15, 15),
                        text_size=10)"""

#### CODE BY ZeroToMastery TensorFlow course.
