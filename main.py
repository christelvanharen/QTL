from scipy.stats import chisquare


def markers_finder(file):
    i = 1
    genes = []  # gen1, gen2
    markers = []  # aaabbbaaa, aa
    for regel in file:
        if ("; " + str(i)) in regel:
            gen = regel.split(" ")[0]
            genes.append(gen)
            marker = file.readline().rstrip().replace(" ", "")
            markers.append(marker)
            i += 1
    return genes, markers


def chisq_test(genes, markers):
    for marker in markers:
        length = len(marker)
        count_a = marker.count("a")
        count_b = marker.count("b")
        print(genes[markers.index(marker)], length, count_a, count_b)
        chis = chisquare([count_a, count_b])
        print(chis)


def compair_dif(genes, markers):
    differences = []
    for i in range(len(markers)):
        for j in range(i + 1, len(markers)):
            print("dif: ", genes[i], genes[j])
            calculate_dif(markers[i], markers[j])


def calculate_dif(marker_a, marker_b):
    difference = 0
    stripes = 0
    for i in range(len(marker_a)):
        if marker_a[i] == "-" or marker_b[i] == "-":
            stripes += 1
        else:
            if marker_a[i] != marker_b[i]:
                difference += 1
    print(difference)
    rf = difference/(len(marker_a)-stripes)*100
    print(rf)
    print(stripes)


def main():
    file = open("CvixLer-MarkerSubset-LG1.txt")
    genes, markers = markers_finder(file)
    # chisq_test(genes, markers)
    compair_dif(genes, markers)


main()
