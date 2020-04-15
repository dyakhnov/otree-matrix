from ._builtin import Page, WaitPage
from .models import Constants
from .utils import slice_list

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class WorkPage(Page):
    timer_text = 'Time left to complete this round:'
    timeout_seconds = Constants.task_time

    form_model = 'player'
    form_fields = ['answer']

    def vars_for_template(self):
        data = self.player.participant.vars['data'][self.round_number-1]
        return {
            'mat1': slice_list(data['list_x'], Constants.diff),
            'mat2': slice_list(data['list_y'], Constants.diff),
            'ca': data['correct_answer']
        }


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'check_answers'


class Results(Page):
    def vars_for_template(self):
        return {
            'num_rounds': Constants.num_rounds,
            'round': self.round_number,
            'players': self.group.get_players()
        }


page_sequence = [
    Introduction,
    WorkPage,
    ResultsWaitPage,
    Results
]
