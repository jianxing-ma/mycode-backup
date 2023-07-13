#!/usr/bin/env python3
""" List Challenge """

import random

def main():
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden',
                  'Craig', 'Deja', 'Elihu', 'Eric',
                  'Giovanni', 'James', 'Joshua', 'Maria',
                  'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit',
                  'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    print(tlgstudents)

    wordbank.append(4)

    num = input("enter a number between 0 and 20: ")
    student_name = tlgstudents[int(num)]

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
