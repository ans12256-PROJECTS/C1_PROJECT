# Assesment #3, Question 2
from scipy import stats

def calculate_t_test(sample1, sample2, type_I_error_rate):
    '''Evaluates whether the two samples come from a population with the same
    population mean.  Returns a tuple containing the p-value for
    the pair of samples and True or False depending if the p-value is
    considered significant at the provided Type I Error Rate (i.e. false
    positive rate, i.e. alpha).
    You may use imports for this question.

    Parameters
    ----------
    sample1, sample2: NumPy array, NumPy array
    type_I_error rate: float

    Returns
    -------
    float, boolean
    '''
    p = stats.ttest_ind(sample1, sample2, equal_var=True)[1]
    return p, p <= type_I_error_rate
