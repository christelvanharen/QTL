from scipy.stats import chisquare


def markers_finder(file):
    i = 1
    genes = []  # gen1, gen2
    markers = []  # aaabbbaaa, aabbbaaa
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
    rf_list = []
    for i in range(len(markers)):
        for j in range(i + 1, len(markers)):
            # print("dif: ", genes[i], genes[j])
            sub_list = [genes[i], genes[j]]
            sub_list.append(calculate_dif(markers[i], markers[j]))
            rf_list.append(sub_list)
    # print(rf_list)
    order_genes(rf_list)


def order_genes(rf_list):
    order_list = []
    higest_rf = 0
    for sub_list in rf_list:
        if sub_list[2] > higest_rf:
            higest_rf = sub_list[2]
            gen_name_one = sub_list[0]
            gen_name_two = sub_list[1]

    print(higest_rf, gen_name_one, gen_name_two)
    order_list.append([gen_name_one, 0])
    for sub_list in rf_list:
        if sub_list[0] == gen_name_one or sub_list[1] == gen_name_one:
            print(sub_list)


def calculate_dif(marker_a, marker_b):
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


# def make_file():
#     file = open("MapChart_file.txt", "w+")


def main():
    file = open("CvixLer-MarkerSubset-LG1.txt")
    genes, markers = markers_finder(file)
    # chisq_test(genes, markers)
    compair_dif(genes, markers)


main()
