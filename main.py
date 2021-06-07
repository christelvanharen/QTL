# QTL project course 8, assignment 1
# By Jasper Versantvoort & Christel van Haren
# June 4th, 2021

from scipy.stats import chisquare


def markers_finder(file):
    """
    The marker subset file is being read. And the genes and markers
    will be separated in 2 lists.
    :param file: The marker subset file
    :return: The genes and the markers from the file in lists.
    """
    i = 1
    genes = []  # gen1, gen2
    markers = []  # aaabbbaaa, aabbbaaab
    for regel in file:
        if ("; " + str(i)) in regel:
            gen = regel.split(" ")[0]
            genes.append(gen)
            marker = file.readline().rstrip().replace(" ", "")
            markers.append(marker)
            i += 1
    return genes, markers


def chisq_test(genes, markers):

    """
    Comparing the differences from the markers with the genes.
    :param genes: The gene names including the markers.
    :param markers: The markers of the genes.
    :return: The chisquare values of all te gene and markers.
    """
    for marker in markers:
        length = len(marker)
        count_a = marker.count("a")
        count_b = marker.count("b")
        print(genes[markers.index(marker)], length, count_a, count_b)
        chis = chisquare([count_a, count_b])
        print(chis)


def compair_dif(genes, markers):
    """
    Comparing the differences from the markers with the genes.
    :param genes: The gene names including the markers.
    :param markers: The markers of the genes.
    :return: A list comparing 2 genes each time with each other with
    the differences between the markers.
    """
    rf_list = []
    for i in range(len(markers)):
        for j in range(i + 1, len(markers)):
            sub_list = [genes[i], genes[j],
                        calculate_dif(markers[i], markers[j])]
            rf_list.append(sub_list)
    order_genes(rf_list)


def order_genes(rf_list):
    """
    The genes are ordered here. It takes the lowest and the highest
    rf there is and then it works its way from outside to the inside.
    :param rf_list: A list comparing 2 genes each time with each
    other with the differences between the markers.
    :return: order_list; A list comparing 2 genes each time with each
    other with the differences between the markers on the right
    order. From low to high.
    """
    order_list = []
    higest_rf = 0
    for sub_list in rf_list:
        if sub_list[2] > higest_rf:
            higest_rf = sub_list[2]
            gen_name_one = sub_list[0]
            gen_name_two = sub_list[1]

    print(higest_rf, gen_name_one, gen_name_two)
    order_list.append([gen_name_one, 0])

    placed = []
    for i in range(19):

        lowest = 0
        gen_name_lowest = ""
        distance = []
        for sub_list in rf_list:
            if sub_list[0] == gen_name_one or sub_list[1] == gen_name_one:
                if lowest == 0 or lowest > sub_list[2]:
                    if sub_list[0] not in placed and sub_list[1] not in placed:
                        lowest = sub_list[2]
                        if sub_list[0] == gen_name_one:
                            gen_name_lowest = sub_list[1]
                        else:
                            gen_name_lowest = sub_list[0]

            print(sub_list)
            distance.append(sub_list)
        placed.append(gen_name_lowest)
        order_list.append([gen_name_lowest, lowest])

    print(order_list)
    make_file_ordering(distance)
    make_file(order_list)


def calculate_dif(marker_a, marker_b):
    """
    Checking if there is a difference or a similarity between the
    positions. The positions can only contain an a or a b.
    :param marker_a: Checking if marker_a shows similarity between
    marker_a and marker_b
    :param marker_b: Checking if marker_b shows a difference between
    marker_a and marker_b
    :return: rf; the difference between the 2 genes.
    """
    difference = 0
    stripes = 0
    for i in range(len(marker_a)):
        if marker_a[i] == "-" or marker_b[i] == "-":
            stripes += 1
        else:
            if marker_a[i] != marker_b[i]:
                difference += 1

    rf = difference / (len(marker_a) - stripes) * 100

    return rf


def make_file(order_list):
    """
    Making a file for MapChart, with the genes and the distances.
    :param order_list: The list with the genes and distances in the
    correct order.
    :return: The txt file for MapChart.
    """
    file = open("MapChart_file.txt", "w+")
    for sub_list in order_list:
        file.write(sub_list[0] + "\t" + str(sub_list[1]) + "\n")


def make_file_ordering(dis):
    file = open("Distance_file.txt", "w+")
    for sub_list in dis:
        file.write(sub_list[0] + "\t" + str(sub_list[1]) + "\t" +
                   str(sub_list[2]) + "\n")


def main():
    file = open("CvixLer-MarkerSubset-LG1.txt")
    genes, markers = markers_finder(file)
    compair_dif(genes, markers)


main()
