# Copyright Afrizal F.A - ICWR-TEAM

print("""
####################################
# R-Searcher - Forensic Tool       #
# Searcher Word on File -          #
# Coded By Afrizal F.A - ICWR-TEAM #
####################################
""")

import os

class search:

    def scan(self, path):

        scan_dir = os.scandir(path)

        for x in scan_dir:

            try:

                name_file = "{}\\{}".format(path, x.name)

                if os.path.isfile(name_file):

                    line_number = 0

                    for per_line in open(name_file, errors='ignore'):

                        line_number += 1

                        if self.word in per_line:

                            print("\t[+] [Match -> \"{}\"] [{} -> Line: {}]".format(self.word, name_file, line_number))
                            open("result-search.txt", "a").write("{} -> Line: {}\n".format(name_file, line_number))

                        else:

                            print("\t[-] [Not Match -> \"{}\"] [{} -> Line: {}]".format(self.word, name_file, line_number))

                elif os.path.isdir(name_file):

                    print("[*] [Is Dir] [{}]".format(name_file))
                    self.scan(name_file)

            except:

                print("[-] [Error] [{}]".format(name_file))

    def __init__(self):

        path_to_scan = input("[*] [Path To Scan] : ")
        self.word = input("[*] [Scan Word] : ")
        self.scan(path_to_scan)

search()
