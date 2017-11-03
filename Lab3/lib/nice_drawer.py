import matplotlib.pyplot as plt


def draw(friends_lst):
    ages_count_dict = {}

    for friend in friends_lst:
        if friend['age'] in ages_count_dict:
            ages_count_dict[friend['age']] += 1
        else:
            ages_count_dict[friend['age']] = 1

    x_axis = []
    y_axis = []

    for x, y in ages_count_dict.items():
        x_axis.append(x)
        y_axis.append(y)

    plt.bar(x_axis, y_axis, align='center')

    plt.ylabel('Number of friends')
    plt.xlabel('Friends\' ages')
    plt.show()
