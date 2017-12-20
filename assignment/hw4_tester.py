


"""
   _   ___        ___  _    _____        _
  | | | \ \      / | || |  |_   ____ ___| |_ ___ _ _
  | |_| |\ \ /\ / /| || |_   | |/ _ / __| __/ _ | '__|
  |  _  | \ V  V / |__   _|  | |  __\__ | ||  __| |
  |_| |_|  \_/\_/     |_|    |_|\___|___/\__\___|_|

"""

import sys



ALL_TESTS = {
    11: dict(
        seif_string = 'Q11',
        function = acc,
        func_name = "acc",
        total_grade = 6,
        tests = [
            dict(
                args=(lambda x,y:x^y,0,[13,24,57,63],), 
                expected=19, 
                symbol='T11_1', 
                grade=2),
            dict(
                args=(lambda x,y:x*y,1,[3,4,5,6],), 
                expected=360, 
                symbol='T11_2', 
                grade=2),
            dict(
                args=(lambda x,y:(x+y),10,[],), 
                expected=10, 
                symbol='T11_3', 
                grade=2),
            ],
        ),
    12: dict(
        seif_string = 'Q12',
        function = myProd,
        func_name = "prod",
        total_grade = 2,
        tests = [
            dict(
                args=([1,1,1,1,1],), 
                expected=1, 
                symbol='T12_1', 
                grade=1),
            dict(
                args=([1,2,3,4,5],), 
                expected=120, 
                symbol='T12_2', 
                grade=1),
            ],
        ),
    13: dict(
        seif_string = 'Q13',
        function = lambda lst,x,res: compose(lst)(x)==res,
        func_name = "compose",
        total_grade = 6,
        tests = [
            dict(
                args=([lambda x:x**2, lambda x:x+6,lambda x: x/2,lambda x:x],10,121,), 
                expected=True, 
                symbol='T13_1', 
                grade=2),
            dict(
                args=([],10,10,), 
                expected=True, 
                symbol='T13_2', 
                grade=2),
            dict(
                args=([lambda x:x**2,lambda x:x**2, lambda x:x**2],7,5764801,), 
                expected=True, 
                symbol='T13_3', 
                grade=2),            
            ],
        ),
    21: dict(
        seif_string = 'Q21',
        function = profit,
        func_name = "profit",
        total_grade = 10,
        tests = [
            dict(
                args=([1,5,8,9],4),
                expected=10,
                symbol='T21_1',
                grade=3),
            dict(
                args=([1,2,7,8,9,12,13],6),
                expected=14,
                symbol='T21_2',
                grade=3),
            dict(
                args=([2,3,5,7,8,9,12,14,17],8),
                expected=16,
                symbol='T21_3',
                grade=4),
            ],
        ),
    22: dict(
        seif_string = 'Q22',
        function = profit2,
        func_name = "profit2",
        total_grade = 8,
        tests = [
            dict(
                args=([1,5,8,9],4),
                expected=10,
                symbol='T22_1',
                grade=2),
            dict(
                args=([1,2,7,8,9,12,13],6),
                expected=14,
                symbol='T22_2',
                grade=3),
            dict(
                args=([2,3,5,7,8,9,12,14,17],8),
                expected=16,
                symbol='T22_3',
                grade=3),
            ],
        ),        
    23: dict(
        seif_string = 'Q23',
        function = profit3,
        func_name = "profit3",
        total_grade = 6,
        tests = [
            dict(
                args=([1,5,8,9],4),
                expected=10,
                symbol='T23_1',
                grade=2),
            dict(
                args=([1,2,7,8,9,12,13],6),
                expected=14,
                symbol='T23_2',
                grade=2),
            dict(
                args=([2,3,5,7,8,9,12,14,17],8),
                expected=16,
                symbol='T23_3',
                grade=2),
            ],
        ),  
    31: dict(
        seif_string = 'Q31',
        function = win,
        func_name = "win",
        total_grade = 8,
        tests = [
            dict(
                args=(9,[1]),
                expected=True,
                symbol='T31_1',
                grade=1),
            dict(
                args=(10,[1]),
                expected=False,
                symbol='T31_2',
                grade=1),                
            dict(
                args=(20,[1,2,3,4,5]),
                expected=True,
                symbol='T31_3',
                grade=2),
            dict(
                args=(20,[1,2,3,4]),
                expected=False,
                symbol='T31_4',
                grade=2),                
            dict(
                args=(15,[1,2,7]),
                expected=False,
                symbol='T31_5',
                grade=2),
            ],
        ), 
    32: dict(
        seif_string = 'Q32',
        function = win2,
        func_name = "win2",
        total_grade = 8,
        tests = [
            dict(
                args=(9,[1]),
                expected=True,
                symbol='T31_1',
                grade=1),
            dict(
                args=(10,[1]),
                expected=False,
                symbol='T31_2',
                grade=1),                
            dict(
                args=(20,[1,2,3,4,5]),
                expected=True,
                symbol='T31_3',
                grade=2),
            dict(
                args=(20,[1,2,3,4]),
                expected=False,
                symbol='T31_4',
                grade=2),                
            dict(
                args=(15,[1,2,7]),
                expected=False,
                symbol='T31_5',
                grade=2),
            ],
        ),         
}

def run_with_limited_time(func, args=(), kwargs={}, timeout_duration=10):
    '''This function will spwan a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    '''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None
        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = (sys.exc_info()[0], sys.exc_info()[1])
        def stop(sefl):
            super(self)

    it = InterruptableThread()
    it.daemon = True
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return [True, it.result]
    else:
        return [False, it.result]

def t(n=0):
    print('Starting tester')
    err_l = []
    err_s = []
    grade = 0

    for seif in ALL_TESTS:
        if n == 0 or seif == n or n == -1:
            function = ALL_TESTS[seif]['function']
            tests = ALL_TESTS[seif]['tests']
            seif_string = ALL_TESTS[seif]['seif_string']
            total_grade = ALL_TESTS[seif]['total_grade']
            func_name = ALL_TESTS[seif]['func_name']
            time_to_run = ALL_TESTS[seif].get('time_to_run', 20)
            tmp_grade = 0
            tmp_errs = []
            if (n != -1):
                print("Test %s: %s: (%d)" % (func_name, seif_string, total_grade))

            for test in tests:
                exception_symbol = test['symbol'] + "_x"
                timeout_symbol = test['symbol'] + "_t"
                reduce = False
                timeout = run_with_limited_time(function, test['args'], {}, time_to_run)
                if timeout[0]:
                    err_l.append("%s: Timeout in %s (running time was longer than %d seconds) - [%s] - (%d)\n" % (seif_string, func_name, time_to_run, timeout_symbol, test['grade']))
                    reduce = True
                    symbol = timeout_symbol
                else:
                    res = timeout[1]
                    if (isinstance(res, tuple)):
                        e = timeout[1][1]
                        err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                        reduce = True
                        symbol = exception_symbol
                    else:
                        try:
                            if res != test['expected']:
                                err_l.append("%s: Error in %s - [%s] - (%d)" % (seif_string, func_name, test['symbol'], test['grade']))
                                err_l.append("Expected: " + str(test['expected']))
                                err_l.append("Got:      " + str(res) + "\n")
                                reduce = True
                                symbol = test['symbol']
                        except:
                            e = sys.exc_info()[1]
                            err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                            reduce = True
                            symbol = exception_symbol

                if reduce:
                    err_s.append(symbol)
                    grade -= test['grade']

    if (n != -1):
        print()
        print("\n".join(str(err) for err in err_l))
        print(grade)

    return [str(grade)]+err_s

test_results = t(-1)

