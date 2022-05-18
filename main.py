
import yaml
import csv

def getAssignment(s,path, result):
    for key in s.keys():
        if "assignment" in key:
            result.append((path + '/' + key, key, s[key]))
        else:
            getAssignment(s[key], path + '/' + key, result)


def main():
     filename = "data1.yml"
     stream = open(filename, 'r')
     yml_dict = yaml.safe_load(stream)
     result = []
     getAssignment(yml_dict, filename, result)
     result.sort(key = lambda x: x[1])
     csvfile = open('sample_output.csv', 'w', newline = ' ')
     writer = csv.writer(csvfile)
     writer.writerow(("assignment_id", "highest_grade"))
     for item in result:
         highest_grade = 0
         student = ""
         scores = item[2]
         for name in scores:
             if float(scores[name]) > highest_grade:
                 highest_grade = float(scores[name])
                 student = name
         writer.writerow((item[0], student))
         main()



