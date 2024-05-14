import sys
import argparse

class AttendencePatterns:
    possible_patterns = None
    def _calc_patterns(self, n:int, pattern:str):
        if n == 0:
            return [pattern]
        if pattern[-3:] == '000':
            return self._calc_patterns(n-1, pattern+'1')
        else:
            return self._calc_patterns(n-1, pattern+'0') + self._calc_patterns(n-1, pattern+'1')

    def all_possible_ways_to_attend_classes(self, days:int):
        self.possible_patterns = self._calc_patterns(days-1, '1') + self._calc_patterns(days-1, '0')
        return self.possible_patterns
    
    def calc_probality(self, days:int):
        possible_patterns = self.all_possible_ways_to_attend_classes(days)
        possible_patterns_of_missing = [i for i in possible_patterns if i[-1] == '0']
        return f"{len(possible_patterns_of_missing)}/{len(possible_patterns)}"
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="provide days to calculate probability ")
    parser.add_argument("--days", type=int, help="No. of days")
    args = parser.parse_args()

    if args.days < 1:
        print("provide number of days")
        sys.exit(1)
    x = AttendencePatterns().calc_probality(args.days)
    print("Probability calculations : ", x)

