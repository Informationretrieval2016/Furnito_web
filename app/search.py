from common import Common

class Search:

    def __init__(self):
        self.com = Common()

    def search_hardmatch(self, name):
    	'''
        #usage: A search function for test
        #arg: search query
        #return: path of json files which contain search query
    	'''
        src = '/home/boyang/Documents/furnitures';
        furniture_list = self.com.GetFileList(src)
        for furniture in furniture_list:
            if name not in furniture:
                furniture_list.remove(furniture)
        return furniture_list