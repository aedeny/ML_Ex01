import numpy as np


class Hypothesis:
    def __init__(self, dimension):
        self.dimension = dimension
        self.hypothesis = [1 for i in range(2 * dimension)]

    def is_correct(self, example, tag):
        if tag == 0:
            return True

        hypothesis_result = True
        for i in range(self.dimension * 2):
            if self.hypothesis[i] == 1:
                if i % 2 == 0:
                    hypothesis_result = example[i / 2] and hypothesis_result
                else:
                    hypothesis_result = not example[i / 2] and hypothesis_result

        return hypothesis_result == tag

    def improve(self, example):
        for i in range(len(example)):
            if example[i] == 1:
                self.hypothesis[2 * i + 1] = 0
            else:
                self.hypothesis[2 * i] = 0

    def __repr__(self):
        to_print = ""
        should_separate = False

        for k in range(self.dimension * 2):
            if self.hypothesis[k] == 1:
                if should_separate:
                    to_print += ","
                    should_separate = False

                if k % 2 == 0:
                    to_print += "not(x" + str(k / 2 + 1) + ")"
                else:
                    to_print += "x" + str(k / 2 + 1)
                should_separate = True

        return to_print


if __name__ == '__main__':
    training_examples = np.loadtxt('data.txt')
    dim = training_examples.shape[1] - 1
    x_matrix = training_examples[:, range(0, dim)].tolist()
    tag_vector = training_examples[:, dim].tolist()

    # Creates the null hypothesis
    h = Hypothesis(dim)

    for k in range(len(x_matrix)):
        if not h.is_correct(x_matrix[k], tag_vector[k]):
            h.improve(x_matrix[k])

    print(h)
