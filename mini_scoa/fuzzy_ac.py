import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from statistics import mean, stdev

'''Declaring the Antecedents'''
roomtemp = ctrl.Antecedent(np.arange(0, 50, 1), "Room Temperature \u00b0C")
roomtemp.automf(names=['Low', 'Normal', 'High', 'Very High'])

humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'Humidity in Percentage (%)')
humidity.automf(names=['Low', 'Normal', 'High'])

bright = ctrl.Antecedent(np.arange(0, 100, 1), 'Brightness in Percentage (%)')
bright.automf(names=['Rainy', 'Cloudy', 'Sunny'])


'''Declaring the Consequents'''
comfort = ctrl.Consequent(np.arange(15, 25, 1), 'Comfortable Temperature in \u00b0C')
comfort.automf(names=['Low', 'Medium', 'High'])

time_in_min = ctrl.Consequent(np.arange(0, 60, 1), 'Time in Minuites')
time_in_min.automf(names=['Very Short Time', 'Short Time', 'Medium Time', 'Long Time', 'Very Long Time'])


'''Declaring the User Defined Membership Functions'''
roomtemp['Low'] = fuzz.gaussmf(roomtemp.universe, mean([0, 0, 15]),stdev([0, 0, 15]))
roomtemp['Normal'] = fuzz.gaussmf(roomtemp.universe, mean([0, 15, 30]), stdev([0, 15, 30]))
roomtemp['High'] = fuzz.gaussmf(roomtemp.universe, mean([15, 30, 45]), stdev([15, 30, 45]))
roomtemp['Very High'] = fuzz.gaussmf(roomtemp.universe, mean([30, 45, 60]), stdev([30, 45, 60]))
roomtemp.view()

humidity['Low'] = fuzz.trimf(humidity.universe, [0,0,40])
humidity['Normal'] = fuzz.trimf(humidity.universe, [10,50,90])
humidity['High'] = fuzz.trimf(humidity.universe, [50,80,120])
humidity.view()

bright['Rainy'] = fuzz.trimf(bright.universe, [0,0,40])
bright['Cloudy'] = fuzz.trimf(bright.universe, [10,50,90])
bright['Sunny'] = fuzz.trimf(bright.universe, [50,80,120])
bright.view()

comfort['Low'] = fuzz.gaussmf(comfort.universe, mean([15, 17, 19]),stdev([15, 17, 19]))
comfort['Medium'] = fuzz.gaussmf(comfort.universe, mean([17, 19, 21]),stdev([17, 19, 21]))
comfort['High'] = fuzz.gaussmf(comfort.universe, mean([19, 21, 23]),stdev([19, 21, 23]))
comfort.view()

time_in_min['Very Short Time'] = fuzz.trimf(time_in_min.universe, [0, 0, 15])
time_in_min['Short Time'] = fuzz.trimf(time_in_min.universe, [0, 15, 30])
time_in_min['Medium Time'] = fuzz.trimf(time_in_min.universe, [15, 30, 45])
time_in_min['Long Time'] = fuzz.trimf(time_in_min.universe, [30, 45, 60])
time_in_min['Very Long Time'] = fuzz.trimf(time_in_min.universe, [45, 60, 60])


'''Define Rules for Fuzzy Control System-1 for AC On Time'''
rule1 = ctrl.Rule(roomtemp['Low'] | humidity['Low'], time_in_min['Very Short Time'])
rule2 = ctrl.Rule(roomtemp['Normal'] | humidity['Low'], time_in_min['Short Time'])
rule3 = ctrl.Rule(roomtemp['Normal'] | humidity['Normal'], time_in_min['Short Time'])
rule4 = ctrl.Rule(roomtemp['Normal'] | humidity['High'], time_in_min['Medium Time'])
rule5 = ctrl.Rule(roomtemp['Normal'] | humidity['High'], time_in_min['Medium Time'])
rule6 = ctrl.Rule(roomtemp['High'] | humidity['Low'], time_in_min['Long Time'])
rule7 = ctrl.Rule(roomtemp['High'] | humidity['Normal'], time_in_min['Long Time'])
rule8 = ctrl.Rule(roomtemp['High'] | humidity['High'], time_in_min['Long Time'])
rule9 = ctrl.Rule(roomtemp['High'] | humidity['High'], time_in_min['Long Time'])
rule10 = ctrl.Rule(roomtemp['High'] | humidity['High'], time_in_min['Very Long Time'])
rule11 = ctrl.Rule(roomtemp['High'] | humidity['High'], time_in_min['Very Long Time'])


'''Define Rules for Fuzzy Control System-1 for Comfortable Temperature'''
fuzz1_rule1 = ctrl.Rule(roomtemp['Very High'] | humidity['High'] | bright['Sunny'], comfort['Low'])
fuzz1_rule2 = ctrl.Rule(roomtemp['Very High'], comfort['Medium'])
fuzz1_rule3 = ctrl.Rule(roomtemp['High'] | humidity['High'] | bright['Sunny'], comfort['Low'])
fuzz1_rule4 = ctrl.Rule(roomtemp['High'] | humidity['High'], comfort['Medium'])
fuzz1_rule5 = ctrl.Rule(roomtemp['Normal'] | humidity['High'] | bright['Sunny'], comfort['Medium'])
fuzz1_rule6 = ctrl.Rule(roomtemp['Normal'] | humidity['High'], comfort['Medium'])
fuzz1_rule7 = ctrl.Rule(roomtemp['Normal'] | humidity['Normal'] | bright['Sunny'], comfort['Medium'])
fuzz1_rule8 = ctrl.Rule(roomtemp['Normal'] | humidity['Normal'] | bright['Cloudy'], comfort['Medium'])
fuzz1_rule9 = ctrl.Rule(roomtemp['Normal'] | humidity['Normal'] | bright['Rainy'], comfort['High'])
fuzz1_rule10 = ctrl.Rule(roomtemp['Low'] | humidity['High'] | bright['Sunny'], comfort['Low'])
fuzz1_rule11 = ctrl.Rule(roomtemp['Low'] | humidity['High'] | bright['Cloudy'], comfort['Low'])
fuzz1_rule12 = ctrl.Rule(roomtemp['Low'] | humidity['High'] | bright['Rainy'], comfort['Medium'])
fuzz1_rule13 = ctrl.Rule(roomtemp['Low'] | humidity['Normal'] | bright['Sunny'], comfort['Medium'])
fuzz1_rule14 = ctrl.Rule(roomtemp['Low'] | humidity['Normal'] | bright['Cloudy'], comfort['Medium'])
fuzz1_rule15 = ctrl.Rule(roomtemp['Low'] | humidity['Normal'] | bright['Rainy'], comfort['High'])
fuzz1_rule16 = ctrl.Rule(roomtemp['Low'] | humidity['Low'] | bright['Sunny'], comfort['Medium'])
fuzz1_rule17 = ctrl.Rule(roomtemp['Low'] | humidity['Low'] | bright['Cloudy'], comfort['Medium'])


'''Train the AC Fuzzy Control System-1'''
ac_ctrl_system_temp = ctrl.ControlSystem([fuzz1_rule1, fuzz1_rule2, fuzz1_rule3, fuzz1_rule4, fuzz1_rule5, fuzz1_rule6,
                                     fuzz1_rule7, fuzz1_rule8, fuzz1_rule9, fuzz1_rule10, fuzz1_rule11, fuzz1_rule12,
                                     fuzz1_rule13, fuzz1_rule14, fuzz1_rule15, fuzz1_rule16, fuzz1_rule17])
ac_ctrl_temp = ctrl.ControlSystemSimulation(ac_ctrl_system_temp)


'''Train the AC Fuzzy Control System-1'''
ac_ctrl_system_time = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6,
                                          rule7, rule8, rule9, rule10, rule11])
ac_ctrl_time = ctrl.ControlSystemSimulation(ac_ctrl_system_time)

'''Take Input from User'''
ac_ctrl_temp.input['Room Temperature \u00b0C'] = 0
ac_ctrl_temp.input['Humidity in Percentage (%)'] = 0
ac_ctrl_temp.input['Brightness in Percentage (%)'] = 0

ac_ctrl_time.input['Room Temperature \u00b0C'] = 0
ac_ctrl_time.input['Humidity in Percentage (%)'] = 0



'''Compute the Output of Fuzzy Control Systems (Comf Temp)/(Time)'''
ac_ctrl_temp.compute()
comfort.view(sim=ac_ctrl_temp)

ac_ctrl_time.compute()
time_in_min.view(sim=ac_ctrl_time)


'''Print And Store Outputs'''
fuzzy_output_temp = ac_ctrl_temp.output['Comfortable Temperature in \u00b0C']
fuzzy_output_time = ac_ctrl_time.output['Time in Minuites']
print('Comfortable Temperature: ', fuzzy_output_temp)
print('Time in Minuites: ', fuzzy_output_time)