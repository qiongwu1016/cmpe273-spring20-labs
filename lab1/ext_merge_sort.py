import os
import heapq
import sys
import numpy as np
import time




class externamMergeSort:
    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.cwd = os.getcwd()
        

    def SortSingleFile(self, path_to_input_file):
        tempBuffer = []
        f = open(path_to_input_file)
        file_name = 'temp_' + path_to_input_file.split('_')[1].split('.')[0]
        path_to_temp = self.cwd + "/temp/"
        if not os.path.exists(path_to_temp):
            os.makedirs(path_to_temp)
        temp_file = open(path_to_temp + file_name, 'w')
        for x in f:
            tempBuffer.append(int(x))
        
        tempBuffer.sort()

        np.savetxt(path_to_temp+file_name, tempBuffer, fmt = '%d')    



    def MiniHeapSort(self, output_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        sorted_file = open(output_path + 'sorted.txt', 'w+')

        file_handler_dict = {}

        min_heap = []
        heapq.heapify(min_heap)
        
        open_files = []
        for f in os.listdir('temp/'):
            if os.path.isfile('temp/' + f):
                file_ = open('temp/' + f)
                open_files.append(file_)
                val = file_.readline()
                is_int = True
                try:
                   # convert to integer
                   int(val)
                except ValueError:
                   is_int = False
                if is_int:
                    heapq.heappush(min_heap, (int(val), 'temp/' + f))
                file_handler_dict['temp/' + f] = file_

        while(len(min_heap) > 0):
            min_element = heapq.heappop(min_heap)
            sorted_file.write(str(min_element[0]) + '\n')
            next_str = file_handler_dict[min_element[1]].readline()
            if next_str:
                heapq.heappush(min_heap, (int(next_str), min_element[1]))
            else:
                file_handler_dict[min_element[1]].close()

        sorted_file.close()

    def sort_input_files(self, input_file_list):
        for file in input_file_list:
             self.SortSingleFile('input/%s'%file)

    def record_time(self, time):
        time_file_name = self.cwd + '/time.txt'
        time_file = open(time_file_name, 'a')
        time_file.write(str(time) + ' seconds\n')
        time_file.close()


start_time = time.time()
obj = externamMergeSort()
input_file_list = os.listdir('input/')
obj.sort_input_files(input_file_list)
obj.MiniHeapSort(obj.cwd + '/output/')
obj.record_time(time.time() - start_time)

