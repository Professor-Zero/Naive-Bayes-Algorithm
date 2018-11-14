
import pandas as pd

training_data_set = pd.read_csv('training.csv')
test_data_set = pd.read_csv('test.csv')
#print(training_data_set)
#print(test_data_set)
size1 = len(training_data_set)
size2 = len(test_data_set)
#print(size1, size2)
manufac_buy_prob = {}
RAM_buy_prob = {}
capacity_buy_prob = {}
warranty_buy_prob = {}
battery_buy_prob = {}
cost_buy_prob = {}
buy_yes_prob = 0
buy_no_prob = 0
#Gets all the possiblities of yes or no for each nominal values.
#all the variables are stored in the above dictionary.
for i, row in training_data_set.iterrows():
    #print(i)
    manufacturer = row[0]
    RAM = row[1]
    capacity = row[2]
    warranty = row[3]
    battery = row[4]
    cost = row[5]
    buy = row[6]
    if manufacturer  not in manufac_buy_prob:
        manufac_buy_prob[manufacturer] = {}
        tempDict = manufac_buy_prob[manufacturer]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1    
    else:
        tempDict = manufac_buy_prob[manufacturer]
        tempDict[buy] += 1  

    if RAM not in RAM_buy_prob:
        RAM_buy_prob[RAM] = {}
        tempDict = RAM_buy_prob[RAM]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1
    else:
        tempDict = RAM_buy_prob[RAM]
        tempDict[buy] += 1

    if capacity not in capacity_buy_prob:
        capacity_buy_prob[capacity] = {}
        tempDict = capacity_buy_prob[capacity]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1
    else:
        tempDict = capacity_buy_prob[capacity]
        tempDict[buy] += 1
    
    if warranty not in warranty_buy_prob:
        warranty_buy_prob[warranty] = {}
        tempDict = warranty_buy_prob[warranty]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1
    else:
        tempDict = warranty_buy_prob[warranty]
        tempDict[buy] += 1

    if battery not in battery_buy_prob:
        battery_buy_prob[battery] = {}
        tempDict =  battery_buy_prob[battery]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1
    else:
        tempDict =  battery_buy_prob[battery]
        tempDict[buy] += 1

    if cost not in cost_buy_prob:
        cost_buy_prob[cost] = {}
        tempDict = cost_buy_prob[cost]
        tempDict["YES"] = 0
        tempDict["NO"] = 0
        tempDict[buy] += 1
    else:
        tempDict = cost_buy_prob[cost]
        tempDict[buy] += 1

    if buy == 'YES':
        buy_yes_prob += 1
    else:
        buy_no_prob += 1

'''print('Manufacturer: ')
print('\t',manufac_buy_prob)
print('RAM: ')
print('\t',RAM_buy_prob)
print('Capacity:')
print('\t',capacity_buy_prob)
print('Warranty: ')
print('\t',warranty_buy_prob)
print('Battery: ')
print('\t',battery_buy_prob)
print('Cost: ')
print('\t',cost_buy_prob)
print('Buy_yes, Buy_no: ')
print(buy_yes_prob,'\t', buy_no_prob)'''

#Computing each P(X and Ci) & P(Ci)
buy_yes_prob = buy_yes_prob/size1
buy_no_prob = buy_no_prob/size1
for key in manufac_buy_prob:
    tempDict = manufac_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1
    
for key in RAM_buy_prob:
    tempDict = RAM_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1

for key in capacity_buy_prob:
    tempDict = capacity_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1

for key in warranty_buy_prob:
    tempDict = warranty_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1

for key in battery_buy_prob:
    tempDict = battery_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1

for key in cost_buy_prob:
    tempDict = cost_buy_prob[key]
    tempDict['YES'] = tempDict['YES']/size1
    tempDict['NO'] = tempDict['NO']/size1

print('Manufacturer: ')
print('\t',manufac_buy_prob)
print('RAM: ')
print('\t',RAM_buy_prob)
print('Capacity:')
print('\t',capacity_buy_prob)
print('Warranty: ')
print('\t',warranty_buy_prob)
print('Battery: ')
print('\t',battery_buy_prob)
print('Cost: ')
print('\t',cost_buy_prob)
print('Buy_yes, Buy_no: ')
print(buy_yes_prob,'\t', buy_no_prob)
    
test_actual_buy_results = {}
test_actual_buy_results['YES'] = 0
test_actual_buy_results['NO'] = 0

for i, row in test_data_set.iterrows():
    #print(i)
    manufacturer = row[0]
    RAM = row[1]
    capacity = row[2]
    warranty = row[3]
    battery = row[4]
    cost = row[5]
    buy = row[6]

    test_actual_buy_results[buy] += 1

    print('Test data', i+1,'~ x =(',manufacturer,',',RAM,',',capacity,',',warranty,',',battery,',',cost,')')
    manufacturer = manufac_buy_prob[manufacturer]
    RAM = RAM_buy_prob[RAM]
    capacity = capacity_buy_prob[capacity]
    warranty = warranty_buy_prob[warranty]
    battery = battery_buy_prob[battery]
    cost = cost_buy_prob[cost]

    manu_prob_yes = manufacturer['YES']/buy_yes_prob
    manu_prob_no = manufacturer['NO']/buy_no_prob

    '''print('\tP(manu, buy=\"yes\"), P(manu, buy=\"no\") ')
    print('\t',manu_prob_yes,'\t', manu_prob_no)
    print()'''

    RAM_prob_yes = RAM['YES']/buy_yes_prob
    RAM_prob_no = RAM['NO']/buy_no_prob

    '''print('\tP(RAM, buy=\"yes\"), P(RAM, buy=\"no\") ')
    print('\t',RAM_prob_yes,'\t', RAM_prob_no)
    print()'''

    capacity_prob_yes = capacity['YES']/buy_yes_prob
    capacity_prob_no = capacity['NO']/buy_no_prob

    '''print('\tP(capacity, buy=\"yes\"), P(capacity, buy=\"no\") ')
    print('\t',capacity_prob_yes,'\t', capacity_prob_no)
    print()'''

    warranty_prob_yes = warranty['YES']/buy_yes_prob
    warranty_prob_no = warranty['NO']/buy_no_prob

    '''print('\tP(warranty, buy=\"yes\"), P(warranty, buy=\"no\") ')
    print('\t',warranty_prob_yes,'\t', warranty_prob_no)
    print()'''

    battery_prob_yes = battery['YES']/buy_yes_prob
    battery_prob_no = battery['NO']/buy_no_prob

    '''print('\tP(battery, buy=\"yes\"), P(battery, buy=\"no\") ')
    print('\t',battery_prob_yes,'\t', battery_prob_no)
    print()'''

    cost_prob_yes = cost['YES']/buy_yes_prob
    cost_prob_no = cost['NO']/buy_no_prob

    '''print('\tP(cost, buy=\"yes\"), P(cost, buy=\"no\") ')
    print('\t',cost_prob_yes,'\t', cost_prob_no)
    print()'''
    prob_no_x = manu_prob_no * RAM_prob_no * capacity_prob_no * warranty_prob_no * battery_prob_no * cost_prob_no
    prob_yes_x = manu_prob_yes * RAM_prob_yes * capacity_prob_yes * warranty_prob_yes * battery_prob_yes * cost_prob_yes
    print('\tP(buy=\'yes\' | X) =', round(prob_yes_x, 7))
    print('\tP(buy=\'no\' | X) =', round(prob_no_x,7) )
    prob_no_x = prob_no_x * buy_yes_prob
    prob_yes_x = prob_yes_x * buy_yes_prob
    print('\tP(buy=\'yes\' | X)*P(buy=\'yes\') =', round(prob_yes_x, 7))
    print('\tP(buy=\'no\' | X)*P(buy=\'no\') =', round(prob_no_x,7) )
    if(prob_yes_x > prob_no_x):
        print('\tThis test X belongs to class Buy=\'yes\'')
    else:
        print('\tThis test X belongs to class Buy=\'no\'')
    print()



