import matplotlib.pyplot as plt
from statistics import mean, stdev
import vals

def SS(lst):
    
    """ Finds sum of squares (SS)
    
    
    Parameters
    ----------
    lst: list of floats and/or integers
    
    Returns
    -------
    sum_of_sq: Sum of squares (SS)
    
    Citations
    ---------
    Formulas: 
        The textbook Statistics by Robert S. White and John S. White, 11th edition
    """
    # Sum of x squared
    sum_xsq = 0
    for num in lst:
        sum_xsq = sum_xsq + num ** 2
    
    # Sum of x
    x_sum = sum(lst)
    
    # Calculating sum of squares
    sum_of_sq = sum_xsq - (x_sum ** 2)/len(lst)
    
    
    return sum_of_sq


# Chooses correct table from vals.py for test and finds critical value
def find_val(directional, sg, d_f):
    
    """ Finds critical value for t tests
    
    
    Parameters
    ----------
    directional: True or False
        Wether or not test is directional
    sg: .05, .01, .001
        Level of significance
    d_f: Degrees of freedom
    
    Returns
    -------
    crit_val: Critical value for t test
    
    Citations
    ---------
    Critical Values (t table): 
        The textbook Statistics by Robert S. White and John S. White, 11th edition
    """
    
    # Picking correct table by checking wether or not test is directional
    if not directional:
        if sg == .05:
            table = vals.non_dir_1
        elif sg == .01:
            table = vals.non_dir_2
        elif sg == .001:
            table = vals.non_dir_3
    elif directional:
        if sg == .05:
            table = vals.dir_1
        elif sg == .01:
            table = vals.dir_2
        elif sg == .001:
            table = vals.dir_3

    # Finds critical value
    # rounds down if df not found in table
    if d_f not in table:
        if d_f > 30 and d_f < 40:
            crit_val = table[30]
        elif d_f > 40 and d_f < 60:
            crit_val = table[40]
        elif d_f > 60 and d_f < 120:
            crit_val = table[60]
        elif d_f > 120 and d_f < 200:
            crit_val = table[120]
        elif d_f >= 200:
            crit_val = table ["inf"]
    else:
        crit_val = table[d_f]
        
    # Returning the critical value    
    return crit_val


def corr_coef(x_list, y_list):
    
    
    """ Find correlation between 2 variables


        Parameters
        ----------
        x_list: List of integers and/or floats
            Values of x
        y_list: List of integers and/or floats
            Values of y

        Returns
        -------
        Plot: Scatter plot of x and y values
        String: Correlation coefficent value r and a warning message
        
        Citations
        ---------
        Formulas: 
        The textbook Statistics by Robert S. White and John S. White, 11th edition
        
        Plotting functions: 
        https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot
        
    """
    
    # Calculates the sum of XY
    sum_1 = 0
    for x_num,y_num in zip(x_list, y_list):
        sum_1 = sum_1 + x_num * y_num
        
    # Calculating the sum of x
    sum_2 = sum(x_list)
    
    # Calculating the sum of y
    sum_3 = sum(y_list)
    
    # Intializing Sum of Products
    SP_xy = sum_1 - (sum_2 * sum_3)/len(x_list)
    
    # Calculating sum of squares for x and y
    SS_x = SS(x_list)
    SS_y = SS(y_list)
    
    # Calculating r 
    r = SP_xy / (SS_x * SS_y) ** (1/2)

    
    # Error message if lists are not same length
    if len(x_list) != len(y_list):
        return("Lists must be same length")
        
    else: 
        # String for plot title
        warning_str = "Remember correlation does not equal causation!"
        
        # Create scatter plot
        plt.scatter(x_list, y_list)
        
        # Adding title to plot
        plt.title(warning_str)
        
        # Set ranges for plot axes
        axis = plt.gca()
        axis.set_ylim([0,100])
        axis.set_xlim([0,100])
        
        # Returns the correlation coeficent
        return r


def t_test_indsamples(list1, list2, directional, sig, sens = "right"):
    
    """Runs a independent samples t-test 


    Parameters
    ----------
    list1: List of integers or floats
    list2: List of integers or floats
    directional: True or False
    Wether or not test is directional
    sig: .05, .01, .001
    Level of significance
    sens: "left" or "right"
    Sensitivity of directional test, default value = "right"

    Returns
    -------
    String: Printed message informing if results are significant
    String: Printed string displaying critical value
    t: t ratio 
    
    Citations
    ---------
    Formulas: 
    The textbook Statistics by Robert S. White and John S. White, 11th edition
    
    Documention for statistics functions (mean, stdev): 
    https://docs.python.org/3/library/statistics.html
    
    Documentation for abs() function: 
    https://docs.python.org/3/library/functions.html?highlight=absolute%20value
    """
    
    # Calculates degrees of freedom
    df = len(list1) + len(list2) - 2
    
    # Finding critical value 
    c_val = find_val(directional, sig, df)
    
    # Averages of list 1 and 2
    x1_bar = mean(list1)
    x2_bar = mean(list2)
    
    # Finds pooled variance
    pool_var = (SS(list1) + SS(list2))/df
    
    # Find estimated standard error for two variables
    s_x1_x2 = ((pool_var/len(list1)) + (pool_var/len(list2))) ** (1/2)
    
    # Calculating t
    t = (x1_bar - x2_bar)/(s_x1_x2)
    
    # Strings for output
    val_str = str(c_val)
    t_str = str(t)
    crit_str = "Critical Value = " + val_str
 
    # String for significant result
    sig_str = "Congrats! The results are significant. Reject the null hypothesis"
    
    # String for non significant result
    non_sig_str = "Darn it! The results are not significant. Fail to reject the null hypothesis"

    # Directional test
    # Checks if t is <= or >= critical value dependending on sensitivity of test
    if directional:
        if sens == "left":
            if t < 0 and t <= -c_val:
                print(sig_str)
            else:
                print(non_sig_str)
        elif sens == "right":
            if t > 0 and t >= c_val:
                print(sig_str)
            else:
                print(non_sig_str)
                
    # Non-directional test
    # Checks if absolute value of t is greater than or equal to critical value. 
    if not directional:
        if abs(t) >= c_val:
             print(sig_str)
        elif abs(t) < c_val:
             print(non_sig_str)
    
    # Print critical value string
    print(crit_str)
    
    return t


def t_test_single(data, hyp_avg, directional, sig, sens = "right"):

    """Runs a single sample t-test 
    
    
    Parameters
    ----------
    data: List of integers or floats
    hyp_avg: Float or integer
        Hypothetical population average
    directional: True or False
        Wether or not test is directional
    sig: .05, .01, .001
        Level of significance
    sens: "left" or "right"
        Sensitivity of directional test, default value = "right"
    
    Returns
    -------
    String: Printed message informing if results are significant
    String: Printed string displaying critical value
    t: t ratio 
    
    Citations
    ---------
    Formulas: 
    The textbook Statistics by Robert S. White and John S. White, 11th edition
    
    Documention for statistics functions (mean, stdev): 
    https://docs.python.org/3/library/statistics.html
    
    Documentation for abs() function: 
    https://docs.python.org/3/library/functions.html?highlight=absolute%20value
    """

    # Finding the degrees of freedom
    df = len(data) - 1

    # Finding critical value
    c_val = find_val(directional, sig, df)

    # Find average for list, data
    avg = mean(data)

    #Estimated standard error of mean of list, data
    # Standard deviation of list, data
    s = stdev(data)
    # Initalizing estimated standard error
    est_error = s/len(data) ** (1/2)

    # Finding t ratio
    t = (avg - hyp_avg)/est_error

    # Strings for output
    val_str = str(c_val)
    crit_str = "Critical Value = " + val_str

    # String for significant result
    sig_str = "Congrats! The results are significant. Reject the null hypothesis"

    # String for non-significant result
    non_sig_str = "Darn it! The results are not significant. Fail to reject the null hypothesis"
    
    # Directional test
    # Checks if t is <= or >= critical value dependending on sensitivity of test
    if directional:
        if sens == "left":
            if t < 0 and t <= -c_val:
                print(sig_str)
            else:
                print(non_sig_str)
        elif sens == "right":
            if t > 0 and t >= c_val:
                print(sig_str)
            else:
                print(non_sig_str)
            
    # Non-directional test
    # Checks if absolute value of t is greater than critical value
    if not directional:
        if abs(t) >= c_val:
            print(sig_str)
        elif abs(t) < c_val:
            print(non_sig_str)

    # Prints critical value string 
    print(crit_str)
    
    # Return t ratio
    return t
