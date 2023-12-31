from linkedList import LinkedList

def main():
    list = LinkedList()
    for x in range(10, 20):
        list.append(x)

    list.info()

    print(f'Element present at index {1}: {list.get(1)}')
    print(f'Value of element present at index {1}: {list.get_value(1)}')

    print('Adding elements to list')
    list.insert(1, 1)
    list.insert(9, 4)
    list.insert(45, 7)
    list.info()
    print()

    print('Removing elements from list')
    list.remove(2)
    list.remove(8)

    list.info()

if(__name__=='__main__'):
    main()