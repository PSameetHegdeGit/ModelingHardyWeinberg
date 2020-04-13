import matplotlib.pyplot as plt

'''
PYTHON MATPLOTLIB NOTES:

First program:
    x = [1,2,3]
    y = [5,7,4]

    plt.xlabel('Plot Number')
    plt.ylabel('Important var')

    plt.title('Practice Graph')

    plt.plot([1,2,3], [5,7,4])

    plt.show()


Second Program:
     x = [1,2,3]
    y = [5,7,4]

    x2 = [1,2,3]
    y2 = [10,14,12]

    plt.plot(x,y, label = 'First Line')
    plt.plot(x2,y2, label = 'Second Line')

    plt.xlabel('Plot Number')
    plt.ylabel ('Important year')

    plt.title('Interesting Graph')

    plt.legend()
    plt.show()

Program 3
    x = [2, 4, 6, 8, 10]
    y = [6,7,8,2,4]

    x2 = [1, 3, 5, 7, 9]
    y2 = [7,8,2,4,2]

    plt.bar(x, y, label =  "Bars1", color='r')
    plt.bar(x2, y2, label='Bars2', color = 'c')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Graph')

    plt.legend()
    plt.show()


**plt.hist(population_ages, bins, histtype='bar', rdwidth=0.8) Graphing a histogram

**plt.scatter(x,y,label='scatter', color = 'k', marker='*", s=10) graphing a scatter plot
'''



if __name__ == "__main__":

    print("I am your father")