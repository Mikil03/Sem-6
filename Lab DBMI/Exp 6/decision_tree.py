class Node():
    def __init__(self, threshold=None, left=None, right=None, info_gain=None, feature_index=None, value=None):
        # for decision node
        self.right = right
        self.left = left
        self.threshold = threshold
        self.feature_index = feature_index
        self.info_gain = info_gain

        # for leaf node
        self.value = value


class DecisionTreeClassifier():
    
    def __init__(self, max_depth=2, min_samples_split=2):
        # initialize the root of tree
        self.root = None

        # stopping conditions
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def build_tree(self, dataset, curr_depth=0):
        X, y = dataset[:, :-1], dataset[:, -1]
        num_samples, num_features = np.shape(X)

        # split until stopping conditions are met
        if num_samples >= self.min_samples_split and curr_depth <= self.max_depth:

            #find the best split
            best_split = self.get_best_split(dataset, num_features, num_samples)

            # check if information gain is positive
            if best_split['info_gain'] > 0:

                # left recursive function
                left_subtree = self.build_tree(
                    best_split["left_dataset", curr_depth+1])

                # right recursive function
                right_subtree = self.build_tree(
                    best_split["left_dataset", curr_depth+1])
                # return decision node
                return Node(best_split["threshold"], left_subtree, right_subtree, best_split["info_gain"], best_split["feature_index"])

        # return leaf node as stopping conditions are met
        leaf_value = self.calculate_leaf_value(y)
        return Node(value=leaf_value)
        

    def get_best_split(self, dataset, num_features, num_samples):
        # dictionary to store values
        best_split = {}
        max_info_gain = -float("inf")

        #loop over all features values present in dataset
        for feature_index in range(num_features):
            feature_values = dataset[:,feature_index]
            possible_thresholds = np.unique(feature_values)

            # loop over all feature values 
            for threshold in possible_thresholds:
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                
                # check if split/child are not empty
                if len(dataset_left)>0 and len(dataset_right)>0:
                    y, left_y, right_y = dataset[:,-1], dataset_left[:,-1], dataset_right[:,-1]
                    # compute information gain
                    curr_info_gain = self.information_gain(y, left_y, right_y, "gini")
                    if curr_info_gain>max_info_gain:
                        best_split["info_gain"] = curr_info_gain
                        best_split["feature_index"] = feature_index
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["threshold"] = threshold
                        max_info_gain = curr_info_gain
        return best_split

    def split(self, dataset, feature_index, threshold):
        dataset_left = np.array([row for row in dataset if row[feature_index]<= threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index] > threshold])
        return dataset_left, dataset_right

    def information_gain(self, parent, left_child, right_child, mode="entropy"):
        weight_l = len(left_child)/len(parent)
        weight_r = len(right_child)/len(parent)

        if mode=="gini":
            gain = self.gini_index(parent) - (weight_l * self.gini_index(left_child) + weight_r * self.gini_index(right_child))
        else:
            gain = self.entropy(parent) - (weight_l * self.entropy(left_child) + weight_r * self.entropy(right_child))
        return gain

    def gini_index(self, y):
        class_labels = np.unique(y)
        gini = 0
        for label in class_labels:
            prob = len(y[y == label]) / len(y)
            gini += prob**2
        return 1 - gini 
            
    def entropy(self, y):
        class_labels = np.unique(y)
        entropy = 0
        for label in class_labels:
            prob = len(y[y == label]) / len(y)
            entropy += -prob * np.log2(prob)
        return entropy

    def calculate_leaf_value(self, y):
        y = list(y)
        return max(y, key=y.count)

    def print_tree(self, tree=None, indent="  "):
        if not tree:
            tree = self.root
        
        if tree.value is not None:
            print(tree.value)
        
        else:
            print("X_"+str(tree.feature_index), "<=", tree.threshold, "?", tree.info_gain)
            print("%sleft:" % (indent), end="")
            self.print_tree(tree.left, indent + indent)
            print("%sright:" % (indent), end="")
            self.print_tree(tree.right, indent + indent)
        
    def fit(self, X, y):
        
        dataset = np.concatenate((X,y),axis=1)
        self.root = self.build_tree(dataset)
    
    def predict(self, X):
        predictions = [self.make_predictions(x, self.root) for x in X]
        return predictions

    def make_predictions(self, x, tree):
        if tree.value != None:
            return tree.value
        feature_value = x[tree.feature_index]
        if feature_value <= tree.threshold:
            return self.make_predictions(x, tree.left)
        else:
            return self.make_predictions(x, tree.left)