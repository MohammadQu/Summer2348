# Mohammad Qureshi
# PSID 1789301
# LAB 10.15



class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def set_name(self, name):
        self.team_name = name

    def set_wins(self, wins):
        self.team_wins = wins

    def set_losses(self, losses):
        self.team_losses = losses



if __name__ =="__main__":

    student_team = Team()
    input_name = str(input())
    input_wins = int(input())
    input_losses = int(input())

    student_team.set_name(input_name)
    student_team.set_wins(input_wins)
    student_team.set_losses(input_losses)
    if(student_team.get_win_percentage() >= 0.5):
        print('Congratulations, Team', student_team.team_name, 'has a winning average!')
    else:
        print('Team', student_team.team_name, 'has a losing average.')

