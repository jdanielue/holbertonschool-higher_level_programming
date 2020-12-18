def search_replace(my_list, search, replace):
        newlist = []
        newlist = list(map(lambda x : replace if (x == search) else x, my_list))
        return newlist
