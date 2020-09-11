class Actor:
    def __init__(self, actor_full_name):
        self.colleague_list = []
        self.actor_full_name = actor_full_name

    def __repr__(self):
        if self.actor_full_name != "" and isinstance(self.actor_full_name, str):
            return "<Actor {}>".format(self.actor_full_name)
        else:
            return "<Actor None>"

    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.colleague_list