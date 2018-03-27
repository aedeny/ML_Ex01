import numpy as np
import sys


class Hypothesis:
    def __init__(self, dimension):
        self.dimension = dimension

        # Creates the null hypothesis
        self.hypothesis = [1 for i in range(2 * dimension)]

    def is_correct(self, example, tag):
        """
        Checks if the hypothesis corresponds to the example.
        :param example: An instance of the training data
        :param tag: The tag of this instance
        :return: True if the hypothesis corresponds to the example, False otherwise.
        """

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
        """
        Improves the hypothesis using the example.
        :param example:
        :return:None
        """
        for i in range(len(example)):
            if example[i] == 0:
                self.hypothesis[2 * i + 1] = 0
            else:
                self.hypothesis[2 * i] = 0

    def __repr__(self):
        """
        :return: A string representing the boolean conjunction in the specified format.
        """
        to_print = ""
        should_separate = False

        for k in range(self.dimension * 2):
            if self.hypothesis[k] == 1:
                if should_separate:
                    to_print += ","

                # Adds literals to the string
                if k % 2 == 0:
                    to_print += "not(x" + str(k / 2 + 1) + ")"
                else:
                    to_print += "x" + str(k / 2 + 1)
                should_separate = True

        return to_print


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("No argument of data file name.")
        exit(-1)

    training_examples = None
    try:
        training_examples = np.loadtxt(sys.argv[1])
    except IOError:
        print("No file named \"" + sys.argv[1] + "\" was found in current directory.")
        exit(-1)
    except ValueError:
        print("Bad file format.")
        exit(-1)

    dim = training_examples.shape[1] - 1
    x_matrix = training_examples[:, range(0, dim)].tolist()
    tag_vector = training_examples[:, dim].tolist()

    # Creates the null hypothesis
    h = Hypothesis(dim)

    # Iterates over the examples and checks if the hypothesis matches the examples.
    # If not, the hypothesis will be improved.
    for k in range(len(x_matrix)):
        if not h.is_correct(x_matrix[k], tag_vector[k]):
            h.improve(x_matrix[k])

    with open('output.txt', 'w') as f:
        f.write(str(h))
    f.close()

    # # Uncomment to print to console
    # print(h)
