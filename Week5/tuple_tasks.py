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
