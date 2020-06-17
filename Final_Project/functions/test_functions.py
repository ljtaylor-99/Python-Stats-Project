import vals

from final import corr_coef, t_test_single, t_test_indsamples

# Test correlation coefficent function
def test_corr_coef():
    
    # Test that function is callable 
    assert callable(corr_coef)
    
    # Test if r is float
    assert type(corr_coef([34, 45, 23],[22, 66, 44])) == float 
    
    # Test if function returns known output 
    assert corr_coef([1, 2, 3],[4, 5, 6]) == 1.0
    

# Test single t test function    
def test_single():
    
    # Test that function is callable 
    assert callable(t_test_single)
    
    # Test if t is float
    assert type(t_test_single([100, 200, 300], 175, 2, .05)) == float
                
    # Test if function returns known output
    assert t_test_single([300, 250, 200], 250, 2, .05) == 0.0


# Test independent samples t test function
def test_indsamples():
    
    # Test that function is callable
    assert callable(t_test_indsamples)
                
    # Test if t is float
    assert type(t_test_indsamples([11, 15, 10], [13, 12, 14], 2, .01)) == float
                
    # Test if function returns known output
    assert t_test_indsamples([1, 2, 3], [2, 2, 2], 2, .05) == 0.0