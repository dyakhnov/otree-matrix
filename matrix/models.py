from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
from .utils import get_random_list


class Constants(BaseConstants):
    name_in_url = 'matrix'
    players_per_group = None
    num_rounds = 2
    task_time = 30
    instructions_template = 'matrix/instructions.html'
    diff = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['data'] = []
            list_x = get_random_list(Constants.diff ** 2)
            list_y = get_random_list(Constants.diff ** 2)
            p.participant.vars['data'].append({
                'list_x': list_x,
                'list_y': list_y,
                'correct_answer': max(list_x) + max(list_y),
                'answer': None
            })


class Group(BaseGroup):
    def check_answers(self):
        for p in self.get_players():
            p.participant.vars['data'][self.round_number - 1]['answer'] = p.answer
            p.is_correct = p.participant.vars['data'][self.round_number - 1]['correct_answer'] == p.answer


class Player(BasePlayer):
    answer = models.IntegerField()
    is_correct = models.BooleanField(default=False)