import re
class Regex(object):
    def pregMatch(self, pattern, content):
        patternCompile = re.compile(pattern)
        return re.search(patternCompile, content)
