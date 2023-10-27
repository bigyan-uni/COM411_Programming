#  return the step with the smallest likelihood of falling
def likelihood():
    #  likelihood a step will fall
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")


#  only called when the file is executed directly
if __name__ == "__main__":
    run_task1()


#  variation to demonstrate how to return a tuple from a function


def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    min_likelihood, max_likelihood = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_likelihood}%")
    print(f"Minimum likelihood of falling: {max_likelihood}%")


run_task2()

#  variation to demonstrate how to nest tuples and lists.


def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run_task3():
    good_steps = []
    bad_steps = []
    step_likelihood = steps()
    for i in range(len(step_likelihood)):
        tup = step_likelihood[i]
        for j in range(len(step_likelihood[i])):
            if j == 1:
                if tup[j] >= 50:
                    bad_steps.append(tup[0])
                else:
                    good_steps.append(tup[0])
    good = len(good_steps)
    bad = len(bad_steps)
    print(f"Good steps: {good}, Bad steps: {bad}")


run_task3()
