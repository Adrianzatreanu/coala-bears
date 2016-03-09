import re

from coalib.bearlib.abstractions.Lint import Lint
from coalib.bears.LocalBear import LocalBear
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


class ObjectiveCLintBear(LocalBear, Lint):
    executable = 'oclint'
    output_regex = re.compile(
    r'(?P<file_name>.*):(?P<line>\d+):(?P<column>\d+): (?P<message>.*)')

    def run(self, filename, file):
        '''
        Checks the code with ``oclint``.

        This bear expects oclint commands to be on your ``PATH``. Please ensure
        /path/to/oclint/bin is in your ``PATH``.
        '''

        self.arguments = ' {filename}'
        self.arguments += ' -- -c'
        return self.lint(filename)
