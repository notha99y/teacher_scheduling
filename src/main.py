from ortools.sat.python import cp_model

NUM_TEACHERS = 4
NUM_SHIFTS = 3
NUM_DAYS = 5

model = cp_model.CpModel()


def create_shifts(num_teachers, num_days, num_shifts):
    '''
    Create shift variables 
    shifts[(t,d,s)]: Teacher 't' works shift 's' on day 'd'


    '''
    shifts = {}
    for t in range(num_teachers):
        for d in range(num_days):
            for s in range(num_shifts):
                shifts[(t, d, s)] = model.NewBoolVar(
                    'shift_{}_{}_{}'.format(t, d, s))


if __name__ == "__main__":
    pass
