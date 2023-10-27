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
