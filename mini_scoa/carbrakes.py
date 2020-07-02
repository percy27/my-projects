def fuzzy(vspeed,vdistance):
    import numpy as np
    import skfuzzy as fuzz
    import matplotlib.pyplot as plt
    from skfuzzy import control as ctrl
    
    distance = ctrl.Antecedent (np.arange ( 0 , 101 , 1 ), 'distance' )
    speed = ctrl.Antecedent (np.arange ( 0 , 101 , 1 ), 'speed' )
    pressure = ctrl.Consequent (np.arange ( 0 , 101 , 1 ), 'pressure' )
    
    distance.automf(names=['poor','mediocre','average','decent','good'])
    speed.automf(names=['poor','mediocre','average','decent','good'])
    
    pressure [ 'much low' ] = fuzz.trimf (pressure.universe, [ 0 , 0 , 25 ])
    pressure [ 'low' ] = fuzz.trimf (pressure.universe, [ 15 , 25 , 50 ])
    pressure [ 'medium' ] = fuzz.trimf (pressure.universe, [ 40 , 50 , 75 ])
    pressure [ 'high' ] = fuzz.trimf (pressure.universe, [ 65 , 75 , 100 ])
    pressure [ 'too high' ] = fuzz.trimf (pressure.universe, [ 90 , 100 , 100 ])
    
    # distance: 'very close' -> 'far away'
    # Available options: 'poor'; 'mediocre'; 'average'; 'decent', or 'good'.
    distance.view ()
    plt.savefig('distance.png')
    speed.view ()
    plt.savefig('speed.png')
    pressure.view ()
    plt.savefig('pressure.png')
    
    rule1 = ctrl.Rule (distance [ 'poor' ] & speed [ 'good' ], pressure [ 'high' ])
    rule2 = ctrl.Rule (distance [ 'mediocre' ] | speed [ 'decent' ], pressure [ 'too high' ])
    rule3 = ctrl.Rule (distance [ 'average' ] | speed [ 'average' ], pressure [ 'high' ])
    rule4 = ctrl.Rule (distance [ 'decent' ] | speed [ 'mediocre' ], pressure [ 'medium' ])
    rule5 = ctrl.Rule (distance [ 'good' ] & speed [ 'poor' ], pressure [ 'much low' ])
    rule6 = ctrl.Rule (distance [ 'good' ] & speed [ 'good' ], pressure [ 'medium' ])
    rule7 = ctrl.Rule (distance [ 'poor' ] & speed [ 'poor' ], pressure [ 'high' ])
    # rule6 = ctrl.Rule (distance ['poor'] | speed ['good'], pressure ['much_alto'])
    # rule7 = ctrl.Rule (distance ['mediocre'] | speed ['decent'], pressure ['high'])
    # rule8 = ctrl.Rule (distance ['average'] | speed ['average'], pressure ['medium'])
    # rule9 = ctrl.Rule (distance ['decent'] | velocity ['mediocre'], pressure ['low'])
    # rule10 = ctrl.Rule (distance ['good'] | speed ['poor'], pressure ['too_thumb'])
    
    
    pressure_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
    amount_pressure = ctrl.ControlSystemSimulation (pressure_ctrl)
    
    amount_pressure.input['distance'] = vdistance
    amount_pressure.input['speed'] = vspeed
    
    # Crunch the numbers
    amount_pressure.compute ()
    
    pressure.view ( yes = amount_pressure )
    
    return amount_pressure.output [ 'pressure' ]
