# -*- coding:utf-8 -*-

#################################
# - Section 1: Module imports - #
#################################

from alfred import Experiment
from alfred.page import Page
from alfred.helpmates import parse_xml_to_dict
import alfred.element as elm
import alfred.section as sec

#################################
# - Section 2: Custom Classes - #
#################################


###################################
# - Section 3: Page Definitions - #
###################################


class Welcome(Page):
    def on_showing(self):
        text_a = elm.TextElement('This is a basic template.', name='text_a')
        text_b = elm.TextElement(self.values.text_b, name='text_b')
        self.append(text_a, text_b)

########################################
# - Section 4: Experiment generation - #
########################################


def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    # file imports
    instr = parse_xml_to_dict(exp.subpath('files/instructions.xml'))
    
    # Define pages
    welcome = Welcome(title='Hello, World', uid='welcome', values=instr)

    # Initialize and fill sections
    main = sec.Section()
    main.append(welcome)

    # Append sections and pages to experiment
    exp.append(main)

    return exp
