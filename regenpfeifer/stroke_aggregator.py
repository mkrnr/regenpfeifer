'''
Created on 27.07.2019

@author: mkoerner
'''


class StrokeAggregator(object):
    '''
    classdocs
    '''

    def aggregate_strokes(self, strokes):
        aggregated_strokes_list = []
        splitted_strokes = strokes.split('/')
        if len(splitted_strokes) > 0:
            prefix = splitted_strokes[0]
            suffix_list = []
            if len(splitted_strokes) > 1:
                suffix_list = self.aggregate_strokes('/'.join(splitted_strokes[1:]))
            if len(suffix_list) > 0:
                for suffix in suffix_list:
                    aggregated_strokes_list.append(prefix + suffix)
                    aggregated_strokes_list.append(prefix + '/' + suffix)
            else:   
                aggregated_strokes_list.append(prefix)

        return aggregated_strokes_list
    
    def aggregate_strokes_list(self, strokes_list):
        aggregated_strokes_list = []
        for strokes in strokes_list:
            aggregated_strokes_list.extend(self.aggregate_strokes(strokes))        return aggregated_strokes_list
    
